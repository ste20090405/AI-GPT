# 06_ProjectRules

本目錄保存《天下風雲錄》專案維護規範。

---

## 包含內容

- 目錄架構
- 命名規範
- Markdown 規範
- Canon 維護原則
- GitHub 維護流程
- 資料衝突處理規則
- 正式更新流程

---

## 核心規則

1. `01_StoryBible` 是最高 Canon。
2. 所有正式資料不得與 Story Bible 衝突。
3. 正式資料直接更新原檔，不建立平行版本。
4. 版本追蹤交由 Git Commit / GitHub History。
5. Patch Notes 記錄版本變更，不取代正式資料。
6. Archive 只作封存，不作為最新資料來源。
7. 所有資料需使用繁體中文與 Markdown。
8. 檔名需清楚、穩定、可搜尋。

---

## 建議流程

```text
提出新增或修正
  ↓
檢查 Story Bible
  ↓
確認無衝突
  ↓
更新對應資料庫
  ↓
更新 Index
  ↓
必要時新增 Patch Notes / Changelog
  ↓
Git Commit
```

---

## 衝突處理

若資料衝突，優先序如下：

1. Story Bible
2. Project Rules
3. World Database
4. Official Character Files
5. Game Data
6. Patch Notes / Changelog
7. Archive
