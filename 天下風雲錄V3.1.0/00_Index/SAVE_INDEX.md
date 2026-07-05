# 天下風雲錄 SAVE_INDEX

Version: v3.1.0-index-refresh
Status: Official
Type: Save Index

---

## Active Save

Active Save: `Save_001`

Path:

`02_Runtime/Save_001/`

---

## Save_001 Files

Required runtime files:

1. `02_Runtime/Save_001/SystemState.md`
2. `02_Runtime/Save_001/CharacterState.md`
3. `02_Runtime/Save_001/CombatState.md`
4. `02_Runtime/Save_001/Timeline.md`
5. `02_Runtime/Save_001/StoryLog.md`
6. `02_Runtime/Save_001/Journal.md`
7. `02_Runtime/Save_001/QuestLog.md`
8. `02_Runtime/Save_001/CharacterMemory.md`
9. `02_Runtime/Save_001/WorldFlags.md`

---

## File Roles

### SystemState.md

Stores current world state, current chapter, time, location, and session-level state.

### CharacterState.md

Stores player character state, including 墨羽's current condition, inventory, abilities, status, and known personal progress.

### CombatState.md

Stores active combat state. If not in combat, this file must remain inactive or neutral.

### Timeline.md

Stores world timeline and major world events. This may include events unknown to 墨羽 if they are required for world simulation.

### StoryLog.md

Stores objective story records of events that occurred during play.

### Journal.md

Stores 墨羽札記 in first-person limited perspective. It must not reveal information 墨羽 does not know.

### QuestLog.md

Stores active, completed, failed, hidden, and suspended quests.

### CharacterMemory.md

Stores people 墨羽 has met or heard about, limited to in-character knowledge.

### WorldFlags.md

Stores machine-readable flags for plot, world state, quest state, and conditional logic.

---

## Default New Game State

If Save_001 has no established game state, initialize:

- World time: `隋・大業七年・春（西元611年）`
- Player: `MC-001 墨羽`
- Chapter: `第一章（待命名）`
- Status: `New Game Initialized`

---

## Save Rules

1. Runtime files are mutable.
2. Canon files are read-only during play.
3. StoryLog and Journal must update after each meaningful player turn.
4. WorldFlags must update when any tracked condition changes.
5. Timeline updates only when time or major world events advance.
