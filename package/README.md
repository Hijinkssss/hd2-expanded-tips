# HD2 Expanded Tips v1.0.0

By Hijinks.

HD2 Expanded Tips replaces the 82 existing US English loading-screen tips with concise, practical reminders about survival, weapons, enemies, objectives, supplies and teamwork.

The familiar TRAINING MANUAL TIPS display and vanilla tip selection stay in place. Tips still appear through the game's original selection behavior; this mod adds no custom rotation or RNG. Version 1.0.0 replaces the existing pool of 82 tips and does not increase its size.

This is a localization resource replacement. It includes no scripts, native hooks, polling, gameplay changes or loader dependency.

## Installation

1. Fully close Helldivers 2.
2. In Steam, browse Helldivers 2's local files and open the `data` folder.
3. Extract the ZIP. Inside `Tips` are three files for archive family `9ba626afa44a3aa3`.
4. Choose an unused patch number N. Check that `9ba626afa44a3aa3.patch_N`, `.patch_N.stream` and `.patch_N.gpu_resources` are all absent. Never overwrite another mod.
5. Rename all three files from `patch_0` to `patch_N`, preserving the suffixes, then copy those three files directly into `data`. Keep the manifest, README and `Tips` folder itself outside `data`.
6. Record the three installed filenames. Start the game with US English selected and check a mission loading screen.

Use a full restart after installation or removal. Install one copy only. A mod manager can renumber or remove manual patches during deployment, so recheck ownership before making changes. The included manifest describes one Tips option; manager import/redeployment of this package has not been live-tested. Manual installation is the documented method.

## Removal

Fully close Helldivers 2. Remove only the three filenames you recorded when installing: `9ba626afa44a3aa3.patch_N`, `9ba626afa44a3aa3.patch_N.stream` and `9ba626afa44a3aa3.patch_N.gpu_resources`, using your chosen N. If a manager has reordered patches, verify that those files still belong to this mod first. Restart the game. Vanilla tips return unless another localization override is active. Do not delete original archives or another mod's files.

## Compatibility and limitations

- US English only. UK English and other language tables are untouched; English fallback is not assumed.
- Built and statically verified against Steam build 25480438. Later game updates need a fresh comparison and may require a rebuild.
- Can conflict with any mod replacing `localization/strings_ui_us.strings`, even if that mod changes different entries. Use one combined override when needed.
- The pool stays at 82 tips. There are no added tip IDs, selector changes or custom randomization.
- Gameplay advice may need revision after balance updates. Wrapping can vary with display settings.
- Earlier v1 rendering and wrapping were confirmed by the author's test report. The polished RC1 game files used for this release passed independent static/archive checks; their final in-game visual spot-check remains pending in the saved project records. No claim is made that all 82 tips have been visually tested.

## Credits

By Hijinks.

Gameplay references: the Helldivers Wiki community and the installed game's own descriptions. Archive format inspection and independent structural checks used FileDiver by xypwn and contributors. Helldivers 2 and its game assets belong to their respective owners. This is an unofficial community mod.

Links: [Helldivers Wiki](https://helldivers.wiki.gg/) | [FileDiver](https://github.com/xypwn/filediver) | [Source and releases](https://github.com/Hijinkssss/hd2-expanded-tips)

## Changelog: 1.0.0

- Initial public v1.0.0 release.
- Replaces all 82 existing US English loading tips with practical advice.
- Includes the RC1 editorial pass: 46 rewrites and one replacement relative to the earlier v1 set; 35 tips retained from that set.
- Preserves the vanilla UI, selector, pool size and all 1,956 unrelated localization entries.
- Uses the exact RC1 main archive and empty sidecars; release metadata and documentation are updated for v1.0.0.
