# 00_Index README

Version: v3.1.0-index-refresh
Status: Official
Type: Repository Navigation Center

---

## Purpose

`00_Index/` is the official navigation, bootstrap and repository index center for 《天下風雲錄 v3.1.0》.

This folder defines:

- official load order
- game start protocol
- project navigation
- save index
- session protocol
- repository map

`00_Index/` does not contain Canon body text, story content, runtime story logs, or duplicated database content.

---

## Repository Map

```text
天下風雲錄V3.1.0/

00_Index/                 Repository index and navigation
01_StoryBible/            Highest Canon source
02_Runtime/               Runtime state and Save data
02_OfficialPatchNotes/    Official Patch Notes and release history
03_Databases/             Official databases
04_Gameplay/              Gameplay rules and presentation
06_Archives/              Deprecated and reference materials
06_ProjectRules/          Project rules and repository standards
07_Documents/             Project documentation and SOP
07_Staging/               Proposals and staging materials
07_Templates/             Templates
08_Tools/                 Validation and utility tools
09_Archive/               Old versions and snapshots
```

---

## Canon Rule

Highest Canon source:

1. `01_StoryBible/`

All project files must follow the Canon priority defined in `LOAD_ORDER.md`.

Canon priority:

```text
Story Bible
    ↓
Runtime
    ↓
Official Databases
    ↓
Gameplay
    ↓
Official Patch Notes
    ↓
Archives
```

---

## Runtime Rule

All live game progress must be stored under:

`02_Runtime/Save_001/`

Runtime files include story logs, journal, world state, character state, timeline, quests, memories, flags, and combat state.

---

## Lazy Loading Rule

Only files listed in `LOAD_ORDER.md` are loaded during boot.

Other character files, maps, martial arts, court data, glossary, events, and archive content are loaded only when required by gameplay.

---

## Related Root Documents

- `README.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
