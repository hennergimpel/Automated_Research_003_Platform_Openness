# Opening the Wrong Work: Contributor Mobility and Software Maintenance Competition

This repository contains the version 2 manuscript and the recorded materials needed to reproduce its synthetic numerical illustration and finite supporting checks.

## Contents

The manuscript source (`paper.md`) and research-process account (`workflow.md`) accompany the model assumptions, derivation, proof and manuscript reviews, exact witness, validation script, saved numerical results, source notes and submission metadata. `T009_reproducibility.zip` is the original local reproduction archive. `manifest.json` is the archive's original file/provenance manifest; `release_manifest.json` records hashes and sizes for the files staged in this repository, excluding itself.

## Reproduction

Requires Python 3.12 or later and the standard library only. From this repository directory, run:

```sh
python T005_validation.py
```

The script checks selected finite price and effort deviations and writes `T005_results.json`. These synthetic calculations corroborate selected cases; they do not prove the continuum equilibrium claims or establish empirical applicability. There is no participant or empirical dataset.

## Provenance and limits

These materials were prepared locally on 22 October 2026. The accompanying `submission_metadata.md` preserves the statement that no public repository existed at that time; it describes that dated local snapshot. This release is intended to make the materials available at [https://github.com/hennergimpel/Automated_Research_003_Platform_Openness](https://github.com/hennergimpel/Automated_Research_003_Platform_Openness).

The repository contains no scholarly fulltexts or extracted conversions, credentials, personal absolute paths, raw task/configuration snapshots or official document template. The original source materials were omitted because redistribution rights were not established; obtain them lawfully for any full document rebuild. Requested model/effort settings are documented, but actual provider model versions and reasoning settings were not independently exposed and remain unknown; token totals are also unavailable. No new analysis rerun or scientific review is claimed for the version 2 editorial update.
