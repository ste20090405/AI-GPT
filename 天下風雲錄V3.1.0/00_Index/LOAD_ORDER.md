# 天下風雲錄
# Official LOAD_ORDER

Version : v3.1.0-final
Status  : Official
Type    : Boot Specification

---

# Purpose

This file defines the official boot order for starting or continuing 《天下風雲錄》.

AI must load files in this order and must not add, skip, or reorder boot files.

---

# Boot Rules

1. Load only the files listed in this document during initialization.
2. Story Bible is the highest Canon.
3. Official Patch Notes may clarify or repair Canon, but may not override Story Bible.
4. Runtime data must be read from `02_Runtime/Save_001/` unless `SAVE_INDEX.md` specifies another active save.
5. Character, map, martial arts, court, glossary, archive, event, and faction data not listed here must use Lazy Loading.
6. When duplicate legacy folders exist, use the v3.1.0 primary paths listed here.
7. Canon and database files are read-only during gameplay.
8. Runtime files are mutable and may be updated during gameplay.

---

# PHASE 1 — Project Bootstrap

README.md

00_Index/README.md

00_Index/Index.md

00_Index/Navigation.md

00_Index/LOAD_ORDER.md

00_Index/SAVE_INDEX.md

00_Index/SESSION_PROTOCOL.md

00_Index/GAME_START.md

---

# PHASE 2 — Core Canon

01_StoryBible/README.md

01_StoryBible/天下風雲錄_Story_Bible_v3.0.3.md

Purpose:

- define world view
- define Canon rules
- define narrative rules
- define historical foundation
- define world-first operation

---

# PHASE 3 — Official Patch Notes

02_OfficialPatchNotes/README.md

02_OfficialPatchNotes/PatchNotes_v3.0.3.md

Purpose:

- apply official fixes
- clarify version rules
- preserve Story Bible priority

---

# PHASE 4 — Runtime Save

02_Runtime/README.md

02_Runtime/GameData_Migration_Notice.md

02_Runtime/Save_001/SystemState.md

02_Runtime/Save_001/CharacterState.md

02_Runtime/Save_001/CombatState.md

02_Runtime/Save_001/Timeline.md

02_Runtime/Save_001/StoryLog.md

02_Runtime/Save_001/Journal.md

02_Runtime/Save_001/QuestLog.md

02_Runtime/Save_001/CharacterMemory.md

02_Runtime/Save_001/WorldFlags.md

Purpose:

- restore current save state
- maintain live story records
- maintain 墨羽札記
- maintain world flags and timeline

---

# PHASE 4.5 — Runtime Validation

After Runtime Save files are loaded, AI must verify Runtime integrity.

Verify:

- `02_Runtime/Save_001/SystemState.md` exists
- `02_Runtime/Save_001/CharacterState.md` exists
- `02_Runtime/Save_001/CombatState.md` exists
- `02_Runtime/Save_001/Timeline.md` exists
- `02_Runtime/Save_001/StoryLog.md` exists
- `02_Runtime/Save_001/Journal.md` exists
- `02_Runtime/Save_001/QuestLog.md` exists
- `02_Runtime/Save_001/CharacterMemory.md` exists
- `02_Runtime/Save_001/WorldFlags.md` exists

If a Runtime file is missing:

1. Create a default empty template for the missing Runtime file.
2. Do not modify Canon, Database, Gameplay, or Project files.
3. Continue boot after Runtime integrity is restored.

Purpose:

- prevent boot failure caused by missing save files
- ensure StoryLog and Journal are always available
- ensure Runtime remains the only mutable gameplay layer

---

# PHASE 5 — Character System

03_Databases/Characters/README.md

03_Databases/Characters/Character Database.md

03_Databases/Characters/Main/MC-001_墨羽_Official_Character_File_v3.0.1.md

Purpose:

- load character index
- load player character file
- do not load all character files at boot

---

# PHASE 6 — World Database

03_Databases/README.md

03_Databases/World/README.md

03_Databases/World/World Database.md

Purpose:

- load world database index
- load official world data
- support history, geography, court, Jianghu, factions, and timeline references

---

# PHASE 7 — Game Systems

04_Gameplay/README.md

04_Gameplay/Game Systems.md

Purpose:

- load runtime rules
- load time, NPC, combat, martial arts, relationship, economy, reputation, quest, and save systems

---

# PHASE 8 — Project Rules and Standards

07_Documents/Standards/Directory_Structure.md

Purpose:

- verify directory structure
- enforce project organization rules

---

# Game Initialization

After all phases are loaded:

1. Establish Session.
2. Determine boot mode: New Game or Continue.
3. Load or create Save according to `SAVE_INDEX.md`.
4. Validate Runtime files.
5. Restore or initialize `SystemState.md`.
6. Restore or initialize `CharacterState.md`.
7. Restore or initialize `Timeline.md`.
8. Restore or initialize `StoryLog.md` and `Journal.md`.
9. Restore or initialize quests, memories, and flags.
10. Initialize current world time.
11. Initialize player character MC-001 墨羽.
12. Begin or continue the active chapter.

Default world start if no runtime state exists:

`隋・大業七年・春（西元611年）`

---

# New Game / Continue Rules

## New Game

If starting a New Game:

1. Create `Save_001` unless another save slot is explicitly specified.
2. Create all required Runtime files if they do not exist.
3. Initialize world time as:

   `隋・大業七年・春（西元611年）`

4. Initialize player character as:

   `MC-001 墨羽`

5. Initialize empty story, journal, quest, memory, timeline, and flag records.
6. Begin Chapter 1.

## Continue

If continuing an existing game:

1. Read `SAVE_INDEX.md`.
2. Identify the active save slot.
3. Load Runtime files from the active save slot.
4. Restore world time, player state, story log, journal, timeline, quests, memories, and flags.
5. Continue from the active chapter and current scene.

If `SAVE_INDEX.md` does not specify an active save, use:

`02_Runtime/Save_001/`

---

# Runtime Update Rule

After every completed player turn, AI must update Runtime records.

Required updates:

- update `StoryLog.md`
- update `Journal.md`
- update `Timeline.md` if world events changed
- update `SystemState.md`
- update `CharacterState.md` if 墨羽's state changed
- update `CombatState.md` if combat state changed
- update `QuestLog.md` if quest state changed
- update `CharacterMemory.md` if character knowledge changed
- update `WorldFlags.md` if flags changed

Journal rule:

- `Journal.md` must only record what 墨羽 knows, feels, witnesses, or reasonably believes.
- It must not reveal hidden world information, future events, or omniscient narration.

StoryLog rule:

- `StoryLog.md` records confirmed events that have occurred in play.
- It may be written in neutral summary form.

Timeline rule:

- `Timeline.md` records world-time changes and major world events.
- Events unknown to 墨羽 may be tracked here only if required for world-state continuity.

---

# Save Rule

Runtime files are mutable.

The following files may change during gameplay:

- `02_Runtime/Save_001/SystemState.md`
- `02_Runtime/Save_001/CharacterState.md`
- `02_Runtime/Save_001/CombatState.md`
- `02_Runtime/Save_001/Timeline.md`
- `02_Runtime/Save_001/StoryLog.md`
- `02_Runtime/Save_001/Journal.md`
- `02_Runtime/Save_001/QuestLog.md`
- `02_Runtime/Save_001/CharacterMemory.md`
- `02_Runtime/Save_001/WorldFlags.md`

The following files are read-only during gameplay:

- Story Bible
- Official Patch Notes
- Official Character Files
- World Database
- Game Systems
- Project Rules
- Index files, unless explicitly performing project maintenance

Gameplay must never rewrite Canon files.

---

# Lazy Loading

Do not load the following at boot unless required by current scene or explicit user request:

- all non-player Character Files
- NPC files
- Historical character files
- Maps
- Martial Arts
- Court database
- Glossary
- Timeline subfiles
- Archives
- Staging files
- AI workflow files
- patch archives
- duplicated legacy folders

Lazy Loading pattern:

Character Database

↓

Find Character ID

↓

Load Official Character File

World Database

↓

Find relevant section or referenced file

↓

Load only required content

---

# Canon Priority

Highest

1. Story Bible
2. Official Patch Notes
3. Official Character Files
4. World Database
5. Game Systems
6. Project Rules and Standards
7. Runtime Save State

Lowest

---

# End

This is the official v3.1.0 final boot order for 《天下風雲錄》.
