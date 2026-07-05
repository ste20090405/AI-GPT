# 天下風雲錄 AUTO_SAVE

Version: v3.1.0-auto-save
Status: Draft
Type: Save Automation Procedure
Based On: `00_Index/SAVE_INDEX.md`

---

## Purpose

本文件依據 `00_Index/SAVE_INDEX.md` 建立自動化存檔流程，用於將當前《天下風雲錄》遊戲狀態寫入 Active Save。

本文件不取代 `SAVE_INDEX.md`，僅將其轉換為可執行的自動化存檔流程說明。

---

## Active Save Source

自動存檔時，必須先讀取：

```text
00_Index/SAVE_INDEX.md
```

並確認：

```text
Active Save: Save_001
Path: 02_Runtime/Save_001/
```

若未來 `SAVE_INDEX.md` 指定其他 Active Save，必須以 `SAVE_INDEX.md` 為準。

---

## Required Runtime Files

自動存檔必須處理以下九個 Runtime 檔案：

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

---

## File Roles

```text
SystemState.md       保存目前世界狀態、章節、時間、地點與 Session 狀態。
CharacterState.md    保存墨羽目前狀態、物品、能力、傷勢、身份與人物進度。
CombatState.md       保存戰鬥狀態；若無戰鬥，保持中立或未啟用。
Timeline.md          保存世界時間線與重大世界事件。
StoryLog.md          保存客觀劇情紀錄。
Journal.md           保存墨羽札記，限第一人稱與墨羽已知資訊。
QuestLog.md          保存進行中、完成、失敗、隱藏、暫停任務。
CharacterMemory.md   保存墨羽已認識或聽聞的人物。
WorldFlags.md        保存劇情旗標、世界狀態與條件判定。
```

---

## Auto Save Core Rules

1. Runtime files are mutable.
2. Canon files are read-only during gameplay.
3. 每次有意義的玩家回合後，`StoryLog.md` 與 `Journal.md` 必須更新。
4. 當任何追蹤條件改變時，`WorldFlags.md` 必須更新。
5. 只有當世界時間或重大世界事件推進時，才更新 `Timeline.md`。
6. 更新既有檔案前，必須先 `fetch_file` 取得最新 blob SHA。
7. 若檔案存在，使用 `update_file`。
8. 若檔案不存在，使用 `create_file`。
9. 不得修改 Canon、Database、Gameplay、Project files，除非使用者明確要求專案維護。
10. `Journal.md` 不得寫入墨羽不知道的情報、未來事件或上帝視角。

---

## Auto Save Sequence

```text
AUTO_SAVE_START

1. Read 00_Index/SAVE_INDEX.md.
2. Determine Active Save path.
3. Build required Runtime file list.
4. For each Runtime file:
   4.1 Try fetch_file(path).
   4.2 If fetch succeeds:
       - read current SHA
       - generate full replacement content
       - update_file(path, sha, content)
   4.3 If fetch fails because file does not exist:
       - generate default Runtime template or current save content
       - create_file(path, content)
5. Confirm every required Runtime file exists.
6. Report updated files and latest commit SHA.

AUTO_SAVE_END
```

---

## Per-File Update Policy

### SystemState.md

Always update after player turn.

Must include:

```text
Current Chapter
Current Scene
World Time
Location
Active Save
Player
Session Status
Next Prompt / Resume Point
```

### CharacterState.md

Update if 墨羽 or important NPC state changed.

Must include:

```text
墨羽年齡
目前身份
公開身份
生命狀態
傷勢
物品
狀態變更紀錄
主要 NPC 狀態
```

### CombatState.md

Update if combat, threat, injury, weapon, martial arts, or combat consequence changed.

If no combat:

```text
Status: 無戰鬥
```

### Timeline.md

Update only when:

```text
World time advances
Major world event changes
Chapter milestone occurs
Historical event enters simulation scope
```

### StoryLog.md

Always update after meaningful player turn.

Rules:

```text
Record only confirmed events that occurred in play.
Neutral objective tone.
Do not record hidden secrets or untriggered future events.
```

### Journal.md

Always update after meaningful player turn.

Rules:

```text
First-person 墨羽 perspective.
Only record what 墨羽 knows, feels, witnesses, believes, or misunderstands.
No omniscient narration.
No hidden NPC motive.
No future information.
```

### QuestLog.md

Update if goals, tasks, quest status, hidden quest state, or completed events changed.

Quest states:

```text
進行中
完成
失敗
中止
隱藏
暫停
待處理
```

### CharacterMemory.md

Update when 墨羽:

```text
Meets a new person
Learns a name
Learns new public information
Changes impression or relationship
Hears about a person
```

### WorldFlags.md

Update when:

```text
Plot flag changes
World condition changes
Quest condition changes
Hidden option condition changes
Relationship gate changes
Historical event trigger condition changes
```

Use minimal necessary flags only.

---

## Existing File Flow

```text
For each Runtime file:

fetch_file(path)
↓
Read sha
↓
Generate complete new content
↓
update_file(path, sha, content)
↓
Record commit SHA
```

---

## Missing File Flow

```text
For each missing Runtime file:

fetch_file(path)
↓
If missing
↓
Generate default template or current content
↓
create_file(path, content)
↓
Record commit SHA
```

---

## Default Runtime Templates

若新建 Runtime 檔案，必須使用對應類型的最小模板。

### SystemState.md

```md
---
title: 天下風雲錄 Save_001 SystemState
save_id: Save_001
status: Active
type: System State
language: zh-TW
---

# Save_001 / SystemState

## 目前章節

```text
待初始化
```

## 目前世界時間

```text
隋・大業七年・春（西元611年）
```
```

### CharacterState.md

```md
---
title: 天下風雲錄 Save_001 CharacterState
save_id: Save_001
status: Active
type: Character State
language: zh-TW
---

# Save_001 / CharacterState

## 玩家角色

```text
姓名：墨羽
狀態：待初始化
```
```

### CombatState.md

```md
---
title: 天下風雲錄 Save_001 CombatState
save_id: Save_001
status: Active
type: Combat State
language: zh-TW
---

# Save_001 / CombatState

## 當前戰鬥狀態

```text
Status: 無戰鬥
```
```

### Timeline.md

```md
# Save_001 / Timeline

## 世界時間線紀錄

```text
待初始化
```
```

### StoryLog.md

```md
# Save_001 / StoryLog

## 劇情紀錄

```text
待初始化
```
```

### Journal.md

```md
# Save_001 / 墨羽札記

## 墨羽札記

```text
待初始化
```
```

### QuestLog.md

```md
# Save_001 / QuestLog

## 主線任務

```text
待初始化
```
```

### CharacterMemory.md

```md
# Save_001 / CharacterMemory

## 已認識人物

```text
待初始化
```
```

### WorldFlags.md

```md
# Save_001 / WorldFlags

## 世界旗標

```text
世界已初始化：否
```
```

---

## Operator Command

建議使用者指令：

```text
@GitHub Save
```

執行時：

```text
1. 讀取 AUTO_SAVE.md。
2. 讀取 SAVE_INDEX.md。
3. 確認 Active Save。
4. 逐一 fetch 九個 Runtime 檔案。
5. 存在則 update_file。
6. 不存在則 create_file。
7. 回報更新結果。
```

---

## Safety Notes

1. 不得把未公開伏筆寫入 `StoryLog.md` 或 `Journal.md`。
2. 不得把墨羽不知道的內容寫入 `Journal.md` 或 `CharacterMemory.md`。
3. 不得用 Archive 內容覆蓋 Runtime。
4. 不得用 Runtime 覆蓋 Canon。
5. 若單一檔案更新失敗，需回報失敗檔案，不得宣稱完整存檔成功。

---

## End

本文件為自動化存檔流程草案。若與 `SAVE_INDEX.md` 衝突，一律以 `SAVE_INDEX.md` 為準。