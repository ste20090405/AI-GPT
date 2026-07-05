# 天下風雲錄 GAME_START

Version: v3.1.0-index-refresh
Status: Official
Type: Game Start Protocol

---

## Purpose

This file defines what happens when the user starts or continues 《天下風雲錄》.

---

## Start Command

When the user says:

`開始《天下風雲錄》`

AI must execute the official boot flow defined by:

`00_Index/LOAD_ORDER.md`

---

## Boot Checklist

1. Load Project Bootstrap files.
2. Load Story Bible v3.0.3.
3. Load Official Patch Notes v3.0.3.
4. Load Runtime Save_001.
5. Load Character Database index.
6. Load MC-001 墨羽.
7. Load World Database.
8. Load Game Systems.
9. Load project structure standard.
10. Restore or initialize game state.

---

## Active Save

Default active save:

`02_Runtime/Save_001/`

Required runtime files:

- `SystemState.md`
- `CharacterState.md`
- `CombatState.md`
- `Timeline.md`
- `StoryLog.md`
- `Journal.md`
- `QuestLog.md`
- `CharacterMemory.md`
- `WorldFlags.md`

---

## Default New Game Setting

If no previous runtime state exists, initialize:

- World time: `隋・大業七年・春（西元611年）`
- Player character: `MC-001 墨羽`
- Chapter: `第一章（待命名）`
- Perspective: first-person limited / 墨羽視角
- World operation: World First

---

## Opening Requirements

When gameplay begins, AI must present:

1. Current world time.
2. Current location if known.
3. Current chapter.
4. Current player state summary.
5. Immediate scene from 墨羽's perspective.
6. Available natural-language action prompt.

---

## Runtime Auto-Record

Every meaningful player turn must update:

- StoryLog
- Journal / 墨羽札記
- QuestLog
- CharacterMemory
- WorldFlags
- Timeline when needed
- SystemState when needed
- CharacterState when needed
- CombatState during combat

---

## Do Not Load at Start

Do not load all files in:

- `03_Databases/Maps/`
- `03_Databases/MartialArts/`
- `03_Databases/Court/`
- `03_Databases/Glossary/`
- `03_Databases/Timeline/`
- `03_Databases/Characters/NPC/`
- `03_Databases/Characters/Templates/`
- `06_Archives/`
- `.github/AI_Workflows/`

Use Lazy Loading only when needed.

---

## Begin

After boot is complete, begin the game with the current scene and await player action.
