# Release workflow

1. Verify RC1 ZIP checksum and all three game files.
2. Update only release documentation/manifest labels; preserve the stable GUID and game-file bytes.
3. Reproduce the game archive from the clean exact-build input and the public tip source. Require the known RC1 hash.
4. Validate the release ZIP CRC, exact five-file layout and game-file identity. Write checksum and provenance.
5. Commit source, documentation, logo, package artifacts and release records to the separate hd2-expanded-tips repository.
6. Create GitHub tag/release v1.0.0 and attach ZIP/checksum/provenance.
7. Create an unpublished Nexus draft for Helldivers 2, complete metadata, upload logo and main file, inspect preview and file record.
8. Stop before Nexus publication. Require explicit user approval of the complete page preview. Never auto-publish or modify another mod/repository.
