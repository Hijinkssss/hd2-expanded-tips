"""Rebuild the exact RC1 game files from a verified user-supplied clean resource."""
from pathlib import Path
import argparse
import hashlib
import json
import struct

def digest(b):
    return hashlib.sha256(b).hexdigest()

def decode(b):
    if struct.unpack_from('<4sIII', b) != (bytes.fromhex('aef3853e'), 1, 2038, 0x03f97b57):
        raise ValueError('Unexpected localization header')
    ids = struct.unpack_from('<2038I', b, 16)
    offsets = struct.unpack_from('<2038I', b, 8168)
    if len(set(ids)) != 2038:
        raise ValueError('Duplicate localization keys')
    values = {}
    for key, offset in zip(ids, offsets):
        if not 16320 <= offset < len(b):
            raise ValueError('Offset outside localization payload')
        values[key] = b[offset:b.index(0, offset)].decode('utf-8')
    return ids, offsets, values

def build(vanilla, specification):
    if digest(vanilla) != specification['original_payload_sha256']:
        raise ValueError('Clean resource SHA-256 mismatch; unsupported build or modified input')
    ids, offsets, values = decode(vanilla)
    entries = specification['entries']
    keys = {int(r['localization_key'], 16) for r in entries}
    if len(entries) != 82 or len(keys) != 82 or not keys <= set(ids):
        raise ValueError('Expected exactly 82 distinct existing tip keys')
    new = bytearray(vanilla)
    permitted = set()
    for index, row in enumerate(entries):
        key = int(row['localization_key'], 16)
        text = row['final_text']
        if row['tip_index'] != index or row['tip_number'] != index+1:
            raise ValueError('Tip order mismatch')
        if not text.isascii() or not 10 <= len(text) <= 85 or not text.endswith('.'):
            raise ValueError('Invalid authored tip')
        if any(x in text for x in ('\0', '\n', '\r', '<', '>', 'PLACEHOLDER', 'EXPANDED TIPS TEST')):
            raise ValueError('Invalid tip marker or formatting')
        pos = 8168 + ids.index(key)*4
        struct.pack_into('<I', new, pos, len(new))
        permitted.update(range(pos, pos+4))
        new.extend(text.encode('utf-8') + b'\0')
    new = bytes(new)
    ids2, offsets2, values2 = decode(new)
    if ids2 != ids or {k for k in ids if values[k] != values2[k]} != keys:
        raise ValueError('Changed key set differs from intended 82')
    if {ids[i] for i in range(2038) if offsets[i] != offsets2[i]} != keys:
        raise ValueError('Unexpected offset change')
    if not {i for i in range(len(vanilla)) if vanilla[i] != new[i]} <= permitted:
        raise ValueError('Unrelated original bytes changed')
    kind = struct.pack('<IIQIIII', 0, 0, 0x0d972bab10b40fd3, 1, 0, 16, 64)
    size = (192 + len(new) + 15) & ~15
    archive = (struct.pack('<III20sQQ24s', 0xf0000011, 1, 1, b'', size, 0, b'')
               + kind + struct.pack('<7Q6I', 0x9524ed24479d06f5, 0x0d972bab10b40fd3,
                                   192, 0, 0, 0, 0, len(new), 0, 0, 16, 64, 0)).ljust(192, b'\0') + new
    archive = archive.ljust(size, b'\0')
    if digest(archive) != specification['expected_archive_sha256']:
        raise ValueError('Rebuilt archive differs from the validated RC1 archive')
    return archive

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vanilla', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads((Path(__file__).resolve().parents[1]/'source/tips.json').read_text(encoding='utf-8'))
    archive = build(args.vanilla.read_bytes(), spec)
    target = args.output/'Tips'
    name = '9ba626afa44a3aa3.patch_0'
    paths = [target/(name+suffix) for suffix in ('', '.stream', '.gpu_resources')]
    if any(p.exists() for p in paths):
        raise FileExistsError('Output already contains game files; choose an empty output directory')
    target.mkdir(parents=True, exist_ok=True)
    for path, data in zip(paths, (archive, b'', b'')):
        with path.open('xb') as handle:
            handle.write(data)
    print('PASS: exact RC1 archive hash; 82 tips replaced; 1,956 unrelated entries preserved.')
    print(digest(archive))

if __name__ == '__main__':
    main()
