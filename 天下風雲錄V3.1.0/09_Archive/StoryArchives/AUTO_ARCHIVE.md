# 天下風雲錄 AUTO_ARCHIVE

Version: v3.1.0-auto-archive
Status: Draft
Type: Story Archive Automation Procedure
Based On: `09_Archive/StoryArchives/README.md`

---

## Purpose

本文件依據 `09_Archive/StoryArchives/README.md` 建立自動化劇情收錄流程，用於將目前遊戲進度封存為 StoryArchives。

封存內容僅供歷史查閱，不作為最新 Canon。

---

## Archive Source

預設使用 Active Save：

```text
SAVE_001
```

讀取來源：

```text
00_Index/SAVE_INDEX.md
02_Runtime/Save_001/SystemState.md
02_Runtime/Save_001/Timeline.md
02_Runtime/Save_001/StoryLog.md
02_Runtime/Save_001/Journal.md
02_Runtime/Save_001/QuestLog.md
02_Runtime/Save_001/CharacterMemory.md
02_Runtime/Save_001/WorldFlags.md
```

若 `SAVE_INDEX.md` 指定其他 Active Save，應以 `SAVE_INDEX.md` 為準。

---

## Archive Target

若使用 `SAVE_001` 進行遊戲，預設收錄至：

```text
09_Archive/StoryArchives/SAVE_01/
```

其他 Save Slot 對應規則：

```text
Save_001 → StoryArchives/SAVE_01/
Save_002 → StoryArchives/SAVE_02/
Save_003 → StoryArchives/SAVE_03/
```

---

## README Rules

收錄時必須遵守 `StoryArchives/README.md`：

```text
1. 保留完整故事敘事。
2. 移除所有互動選項。
3. 文末附上當時 Canon 劇情結束狀態。
4. 僅供歷史查閱，不作為最新 Canon。
```

---

## Volume and Chapter Naming Rule

封存時依章節名稱與卷數建立檔案。

### 卷數資料夾

```text
第001卷/
第002卷/
第003卷/
```

### 章節檔案

```text
第一章.md
第二章.md
第三章.md
第七章（新的早晨・上）.md
```

### 完整路徑範例

```text
09_Archive/StoryArchives/SAVE_01/第001卷/第一章.md
09_Archive/StoryArchives/SAVE_01/第001卷/第二章.md
09_Archive/StoryArchives/SAVE_01/第001卷/第七章（新的早晨・上）.md
```

若目前劇情仍屬同一卷，持續寫入同一卷資料夾。

若章節或劇情明確進入新卷，才建立下一個卷數資料夾。

---

## Archive Input Priority

自動收錄時，來源優先順序如下：

```text
1. FullStory / 已保存完整正文檔案（若存在）
2. StoryLog + Journal + Timeline 重建封存敘事
3. 當前對話中已完整輸出的章節正文
4. 手動提供的章節正文
```

注意：

```text
若無完整正文來源，系統必須標記為「重建封存版」，不得宣稱為逐字原文。
```

---

## Archive Content Format

每個章節封存檔使用以下格式：

```md
# 天下風雲錄

## 第N卷

## 第X章　章節名稱

正文內容……

---

### Canon 劇情結束狀態

- Save：Save_001
- 世界時間：
- 目前地點：
- 墨羽年齡：
- 墨羽公開身分：
- 已登場人物：
- 已完成事件：
- 目前劇情節點：
- 備註：本封存僅供歷史查閱，不作為最新 Canon。
```

---

## Auto Archive Sequence

```text
AUTO_ARCHIVE_START

1. Read 09_Archive/StoryArchives/README.md.
2. Read 00_Index/SAVE_INDEX.md.
3. Determine Active Save.
4. If Active Save is Save_001, set archive root:
   09_Archive/StoryArchives/SAVE_01/
5. Load Runtime files from Active Save:
   - SystemState.md
   - Timeline.md
   - StoryLog.md
   - Journal.md
   - QuestLog.md
   - CharacterMemory.md
   - WorldFlags.md
6. Determine current volume number.
7. Determine current chapter name from SystemState / StoryLog.
8. Generate archive chapter content:
   - keep story narration
   - remove all interaction options
   - remove player prompt blocks
   - remove runtime-only fields not needed in archive body
9. Append Canon 劇情結束狀態.
10. Build target path:
    StoryArchives/SAVE_01/第NNN卷/章節名稱.md
11. Check whether target file exists.
12. If target file exists:
    - fetch SHA
    - update_file
13. If target file does not exist:
    - create_file
14. Report target path and commit SHA.

AUTO_ARCHIVE_END
```

---

## Chapter Detection Rule

章節名稱來源優先順序：

```text
1. SystemState.md Current Chapter
2. StoryLog.md latest 章節
3. Timeline.md current 章節紀錄
4. User supplied chapter name
```

若章節名稱包含小節，例如：

```text
第七章　新的早晨（上）
```

檔案名稱應保留為：

```text
第七章（新的早晨・上）.md
```

---

## Volume Detection Rule

預設：

```text
第001卷
```

只有在以下條件成立時建立新卷：

```text
1. 使用者明確指定新卷。
2. StoryLog / Timeline 記錄已進入新卷。
3. SystemState 明確標示卷數變更。
4. 官方 Canon 或 Patch Notes 指定卷數變更。
```

不得因章節數增加自動切卷。

---

## Interaction Removal Rule

封存時必須移除以下內容：

```text
互動選項 ①～⑤
風險欄位
備註欄位
你要怎麼做？
自由行動提示
隱藏選項觸發狀態
玩家選項輸入紀錄
```

但若「風險」或「備註」已成為劇情正文的一部分，需改寫為自然敘事，不得保留選項格式。

---

## Canon Ending State Rule

每章文末必須附上當時 Canon 劇情結束狀態。

最小欄位：

```text
Save
世界時間
地點
墨羽狀態
公開身分
重要人物
已完成事件
目前劇情節點
Archive Status
```

Archive Status 固定為：

```text
Historical Archive Only / Not Latest Canon
```

---

## Existing File Flow

```text
fetch_file(target_path)
↓
Read SHA
↓
Regenerate full archive content
↓
update_file(target_path, sha, content)
```

---

## Missing File Flow

```text
fetch_file(target_path)
↓
If missing
↓
create_file(target_path, content)
```

---

## Operator Command

建議使用者指令：

```text
@GitHub Archive
```

或：

```text
@GitHub Auto Archive
```

執行時：

```text
1. 讀取 AUTO_ARCHIVE.md。
2. 讀取 StoryArchives README。
3. 讀取 SAVE_INDEX.md。
4. 載入 Active Save Runtime。
5. 判定 Save 對應 StoryArchives/SAVE_XX。
6. 判定卷數與章節名稱。
7. 生成純劇情封存檔。
8. 寫入或更新 Archive。
```

---

## Safety Notes

1. 不得把未公開伏筆寫入封存正文。
2. 不得把墨羽不知道的秘密當作已發生劇情收錄。
3. 不得修改 Runtime、Canon、Database 或 Gameplay 檔案。
4. Archive 為歷史查閱，不得作為最新 Canon。
5. 若無完整正文來源，必須標記為「重建封存版」。
6. 若寫入失敗，必須回報失敗路徑，不得宣稱完整收錄成功。

---

## End

本文件為 StoryArchives 自動化收錄流程草案。若與 `StoryArchives/README.md` 衝突，一律以 `README.md` 為準。