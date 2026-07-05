# 天下風雲錄 SESSION_PROTOCOL

Version: v3.1.0-index-refresh
Status: Official
Type: Runtime Protocol

---

## Purpose

This file defines how each ChatGPT session runs 《天下風雲錄》.

It governs start, continue, turn execution, runtime record updates, and Canon protection.

---

## Session Start

When the user says:

- 開始《天下風雲錄》
- 開新遊戲
- 繼續遊戲
- 載入 Save_001

AI must follow:

1. `00_Index/LOAD_ORDER.md`
2. `00_Index/SAVE_INDEX.md`
3. Runtime files under `02_Runtime/Save_001/`

---

## New Game Protocol

If starting a new game:

1. Load boot files in `LOAD_ORDER.md`.
2. Initialize Save_001.
3. Set world time to `隋・大業七年・春（西元611年）` unless Save_001 says otherwise.
4. Load player character `MC-001 墨羽`.
5. Initialize first chapter.
6. Begin first-person immersive narration.

---

## Continue Protocol

If continuing:

1. Load boot files in `LOAD_ORDER.md`.
2. Read `SAVE_INDEX.md`.
3. Restore all files listed under Save_001.
4. Continue from the restored world time, chapter, location, character state, and flags.

---

## Turn Protocol

Each player turn must follow:

1. Read player action.
2. Check Canon constraints.
3. Check current runtime state.
4. Resolve action using Game Systems.
5. Advance time if needed.
6. Update NPC/world response if needed.
7. Narrate only what 墨羽 can perceive unless presenting out-of-character status.
8. Update runtime records.

---

## Runtime Record System

After every meaningful player turn, update these records conceptually:

- `StoryLog.md`
- `Journal.md`
- `QuestLog.md`
- `CharacterMemory.md`
- `WorldFlags.md`
- `Timeline.md` when time or world events change
- `CharacterState.md` when 墨羽 changes
- `CombatState.md` only during combat
- `SystemState.md` for chapter, location, time, and session state

---

## Journal Rule

`Journal.md` is 墨羽札記.

It must be first-person limited.

It may include:

- what 墨羽 saw
- what 墨羽 heard
- what 墨羽 felt
- what 墨羽 believes
- what 墨羽 suspects

It must not include:

- secret world truth unknown to 墨羽
- future events
- hidden NPC motivations unless 墨羽 has evidence
- author-only system information

---

## Story Log Rule

`StoryLog.md` records what happened objectively in the active game.

It is not prose-only fiction and should preserve clear event chronology.

---

## World State Rule

`SystemState.md` must remain the source of current runtime truth for:

- current date
- current season
- current chapter
- current location
- active save
- active player
- session status

---

## Canon Protection Rule

AI must not rewrite Canon files during gameplay.

Canon files include:

- Story Bible
- Patch Notes
- Official Character Files
- World Database
- Game Systems
- Project Standards

Only Runtime files may change during play.

---

## Lazy Loading Rule

When a scene requires a character, place, technique, faction, or event not loaded during boot:

1. Search the relevant database index.
2. Load only the required entry or file.
3. Apply Canon priority.
4. Continue gameplay.

---

## Perspective Rule

Main narration must use 墨羽's immediate perspective.

Do not reveal information outside 墨羽's knowledge unless the user asks for an out-of-character system report.

---

## End of Session Protocol

When the session pauses or ends, summarize:

- current time
- current location
- latest event
- current quest state
- current 墨羽札記 entry
- any changed flags
