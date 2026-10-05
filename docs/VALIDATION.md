# Release verification

The release preserves the exact main archive and both empty sidecars from v1.0.0-RC1. Exactly 82 known tip values changed compared with the clean game resource; 1,956 unrelated values and their offset words remained identical. No localization IDs were added or removed. Archive structure was independently decoded and checked with FileDiver during RC1 preparation. All original payload bytes are preserved except the 82 tip offset words, with replacement text appended.

Earlier v1 rendered and wrapped successfully according to the author's report. The saved RC1 record still lists its final manual loading-screen spot-check as pending. The historical placeholder screenshot is intentionally not presented as a screenshot of this release. No game was launched for release packaging.

`validation.json` preserves the structural check results and game-file hashes. `SHA256SUMS.txt` records the release download checksum. `release-provenance.json` establishes byte identity of the three released game files with RC1.
