# Release verification

The release preserves the exact main archive and both empty sidecars from v1.0.0-RC1. Exactly 82 known tip values changed compared with the clean game resource; 1,956 unrelated values and their offset words remained identical. No localization IDs were added or removed. Archive structure was independently decoded and checked with FileDiver during RC1 preparation. All original payload bytes are preserved except the 82 tip offset words, with replacement text appended.

Runtime validation PASSED. Three different final RC1 tips were manually observed in-game across separate mission loads, with correct multiline wrapping and vanilla tip selection:

1. “A Resupply box replenishes your supplies and fills an empty Supply Pack slot.”
2. “Going prone reduces blast damage, but does not make you explosion-proof.”
3. “A called-in Hellbomb must be armed at its panel before it detonates.”

These are spot-checks of three real tips, not individual visual inspection of all 82. The historical placeholder screenshot is not evidence for this release.

`validation.json` preserves the structural check results and game-file hashes. `SHA256SUMS.txt` records the release download checksum. `release-provenance.json` establishes byte identity of the three released game files with RC1.
