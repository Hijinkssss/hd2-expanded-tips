# HD2 Expanded Tips

**By Hijinks | v1.0.0**

![HD2 Expanded Tips](assets/HD2-Expanded-Tips.png)

HD2 Expanded Tips replaces the 82 existing US English loading-screen tips with concise, practical reminders about survival, weapons, enemies, objectives, supplies and teamwork.

The familiar TRAINING MANUAL TIPS display and vanilla tip selection stay in place. Tips still appear through the game's original selection behavior; this mod adds no custom rotation or RNG. Version 1.0.0 replaces the existing pool of 82 tips and does not increase its size.

This is a localization resource replacement. It includes no scripts, native hooks, polling, gameplay changes or loader dependency.

## Installation

1. Download `HD2-Expanded-Tips-v1.0.0.zip`.
2. Open HD2 Arsenal.
3. Import the ZIP.
4. Enable **HD2 Expanded Tips**.
5. Deploy your mod configuration.

Launch Helldivers 2 normally through your Arsenal-managed setup.

No additional mod loader or runtime dependency is required.

## Removal

Disable or remove **HD2 Expanded Tips** in Arsenal, then redeploy your mod configuration.

Vanilla loading-screen tips will return unless another mod is replacing the same localization resource.

## Compatibility and limitations

- US English only. UK English and other language tables are untouched; English fallback is not assumed.
- Built for the currently supported Steam build 25480438 and statically verified against it. Future game updates may require a fresh comparison and rebuild.
- Can conflict with mods replacing `localization/strings_ui_us.strings`, even if they change different entries.
- Uses the fixed vanilla pool of 82 tips; no added tip IDs.
- Intended to be installed and deployed through HD2 Arsenal, the recommended method.
- No scripts.
- No Shared Loader/Bingus loader or other runtime mod loader dependency.
- No native hooks.
- No runtime polling.
- No gameplay changes.
- No custom RNG or selector behavior. Vanilla loading-screen tip selection remains intact.
- Gameplay advice may need revision after balance updates. Wrapping can vary with display settings.

## Validation

Runtime validation PASSED. Three different final RC1 tips were manually observed in-game across separate mission loads, including correct multiline wrapping. Different tips were selected by the vanilla loading-screen system. This does not claim that all 82 tips were individually visually inspected.

All 82 intended tip entries were replaced; the other 1,956 localization entries remained unchanged. See [the validation record](docs/VALIDATION.md).

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

## Download

Use [the v1.0.0 release](https://github.com/Hijinkssss/hd2-expanded-tips/releases/tag/v1.0.0) and download `HD2-Expanded-Tips-v1.0.0.zip`. GitHub source archives are for development.

## Build source

`source/tips.json` contains the exact 82 authored replacement texts. `tools/build.py` accepts your own clean extracted US localization resource and verifies its SHA-256 before building. It refuses unknown inputs. See [BUILD.md](BUILD.md).

## Permissions

See [RIGHTS.md](RIGHTS.md). No open-source license has been selected. Game assets are not covered by any permission from this author.
