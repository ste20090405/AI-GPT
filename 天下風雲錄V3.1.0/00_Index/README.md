# 00_Index README

Version: v3.1.0-index-refresh
Status: Official
Type: Index Center

---

## Purpose

`00_Index/` is the official navigation and bootstrap center for 《天下風雲錄》.

This folder defines:

- official load order
- game start protocol
- project navigation
- save index
- session protocol

`00_Index/` does not contain Canon body text, story content, runtime story logs, or duplicated database content.

---

## Canon Rule

Highest Canon source:

1. `01_StoryBible/#U5929#U4e0b#U98a8#U96f2#U9304_Story_Bible_v3.0.3.md`

All project files must follow the Canon priority defined in `LOAD_ORDER.md`.

---

## Runtime Rule

All live game progress must be stored under:

`02_Runtime/Save_001/`

Runtime files include story logs, journal, world state, character state, timeline, quests, memories, flags, and combat state.

---

## Lazy Loading Rule

Only files listed in `LOAD_ORDER.md` are loaded during boot.

Other character files, maps, martial arts, court data, glossary, events, and archive content are loaded only when required by gameplay.
