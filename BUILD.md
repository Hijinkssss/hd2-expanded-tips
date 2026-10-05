# Reproducing the game files

Requires Python 3.10+ and your own clean extracted `localization/strings_ui_us.strings` resource from Steam build 25480438. No proprietary clean resource is included in the source tree. The expected clean SHA-256 is recorded in `source/tips.json`.

```text
python tools/build.py --vanilla PATH_TO_CLEAN_STRINGS --output build
```

The tool changes the 82 authored tip values, checks all other 1,956 values and their offsets, constructs the single-resource patch and checks the exact expected RC1 archive SHA-256. It writes three files under `build/Tips`. Unknown or modified input resources fail before output. It does not install anything, alter the game, or launch the game.

The release ZIP additionally contains the manifest and README from `package/`. `Version: 1` in the manifest is its format version, while the mod release version is 1.0.0. The stable package GUID is preserved from RC1.
