# 天下風雲錄 AUTO_LOAD

Version: v3.1.0-auto-load
Status: Draft
Type: Boot Automation Procedure
Based On: `00_Index/LOAD_ORDER.md`

---

## Purpose

本文件依據 `00_Index/LOAD_ORDER.md` 建立自動化載入流程，用於開始或繼續《天下風雲錄》時，按官方 Boot Order 逐步載入必要檔案。

本文件不取代 `LOAD_ORDER.md`，僅將其轉換為可執行的自動化流程說明。

---

## Core Rules

1. 初始化時只能載入 `LOAD_ORDER.md` 明列的檔案。
2. 不得新增、跳過或重排 Boot 檔案。
3. Runtime 預設讀取 `02_Runtime/Save_001/`，除非 `SAVE_INDEX.md` 指定其他 Active Save。
4. Canon、Database、Gameplay、Project files 在遊戲中唯讀。
5. Runtime files 可於遊戲中更新。
6. 未列於 Boot Order 的角色、地圖、武學、朝廷、詞彙、封存、事件、勢力等資料，必須使用 Lazy Loading。
7. 若 Runtime 檔案缺失，只能建立缺失的 Runtime 空模板，不得修改 Canon 或 Database。

---

## Auto Load Sequence

### PHASE 1 — Project Bootstrap

```text
README.md
00_Index/README.md
00_Index/Index.md
00_Index/Navigation.md
00_Index/LOAD_ORDER.md
00_Index/SAVE_INDEX.md
00_Index/SESSION_PROTOCOL.md
00_Index/GAME_START.md
```

### PHASE 2 — Core Canon

```text
01_StoryBible/README.md
01_StoryBible/天下風雲錄_Story_Bible_v3.0.3.md
```

### PHASE 3 — Official Patch Notes

```text
02_OfficialPatchNotes/README.md
02_OfficialPatchNotes/PatchNotes_v3.0.3.md
```

### PHASE 4 — Runtime Save

```text
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
```

### PHASE 4.5 — Runtime Validation

自動檢查以下檔案是否存在：

```text
02_Runtime/Save_001/SystemState.md
02_Runtime/Save_001/CharacterState.md
02_Runtime/Save_001/CombatState.md
02_Runtime/Save_001/Timeline.md
02_Runtime/Save_001/StoryLog.md
02_Runtime/Save_001/Journal.md
02_Runtime/Save_001/QuestLog.md
02_Runtime/Save_001/CharacterMemory.md
02_Runtime/Save_001/WorldFlags.md
```

若缺失：

```text
1. 建立缺失 Runtime 檔案的預設空模板。
2. 不修改 Canon、Database、Gameplay、Project files。
3. Runtime 完整後繼續 Boot。
```

### PHASE 5 — Character System

```text
03_Databases/Characters/README.md
03_Databases/Characters/Character Database.md
03_Databases/Characters/Main/MC-001_墨羽_Official_Character_File_v3.0.1.md
```

### PHASE 6 — World Database

```text
03_Databases/README.md
03_Databases/World/README.md
03_Databases/World/World Database.md
```

### PHASE 7 — Game Systems

```text
04_Gameplay/README.md
04_Gameplay/Game Systems.md
```

### PHASE 8 — Project Rules and Standards

```text
07_Documents/Standards/Directory_Structure.md
```

---

## Auto Boot Procedure

```text
AUTO_LOAD_START

1. Read 00_Index/LOAD_ORDER.md.
2. Execute PHASE 1 through PHASE 8 in exact order.
3. Read 00_Index/SAVE_INDEX.md.
4. Determine Active Save.
5. If Active Save is missing, use 02_Runtime/Save_001/.
6. Load all Runtime files from Active Save.
7. Validate Runtime integrity.
8. If Runtime file missing, create only missing Runtime template.
9. Determine boot mode:
   - If Runtime has established current chapter and scene: Continue.
   - If Runtime is empty or uninitialized: New Game.
10. Restore or initialize:
   - SystemState
   - CharacterState
   - Timeline
   - StoryLog
   - Journal
   - QuestLog
   - CharacterMemory
   - WorldFlags
11. Initialize current world time.
12. Initialize player character MC-001 墨羽.
13. Begin or continue active chapter.

AUTO_LOAD_END
```

---

## New Game Detection

若 Runtime 尚未建立有效狀態，使用以下預設值：

```text
World Time: 隋・大業七年・春（西元611年）
Player: MC-001 墨羽
Chapter: 第一章
Status: New Game Initialized
```

---

## Continue Detection

若 Runtime 已存在有效狀態，必須恢復：

```text
Current chapter
Current scene
World time
Player state
StoryLog
Journal
Timeline
QuestLog
CharacterMemory
WorldFlags
```

---

## Runtime Update After Player Turn

每次玩家回合完成後，依狀態變化更新：

```text
StoryLog.md          必須更新
Journal.md           必須更新
SystemState.md       必須更新
Timeline.md          世界時間或重大事件推進時更新
CharacterState.md    墨羽狀態變更時更新
CombatState.md       戰鬥狀態變更時更新
QuestLog.md          任務狀態變更時更新
CharacterMemory.md   人物知識變更時更新
WorldFlags.md        旗標變更時更新
```

---

## Lazy Loading Rule

以下資料不得於 Boot 時自動載入，除非當前場景需要或使用者明確要求：

```text
Non-player Character Files
NPC files
Historical character files
Maps
Martial Arts
Court database
Glossary
Timeline subfiles
Archives
Staging files
AI workflow files
Patch archives
Duplicated legacy folders
```

Lazy Loading 流程：

```text
Need data
↓
Use Navigation.md / Database index
↓
Find target file or Character ID
↓
Load only required file or section
↓
Return to current Runtime context
```

---

## Canon Priority During Auto Load

```text
1. Story Bible
2. Official Patch Notes
3. Official Character Files
4. World Database
5. Game Systems
6. Project Rules and Standards
7. Runtime Save State
```

---

## Operator Command

建議使用者指令：

```text
@GitHub Auto Load
```

執行時：

```text
1. 讀取 AUTO_LOAD.md。
2. 讀取 LOAD_ORDER.md。
3. 依 LOAD_ORDER.md 執行完整載入。
4. 驗證 Runtime。
5. 回報 New Game 或 Continue 狀態。
```

---

## End

本文件為自動化載入流程草案。若與 `LOAD_ORDER.md` 衝突，一律以 `LOAD_ORDER.md` 為準。