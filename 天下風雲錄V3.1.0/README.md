# 天下風雲錄 Official Repository

> Official Canon Repository for **天下風雲錄 v3.1.0**

---

# Quick Start

```text
新對話
    ↓
@GitHub Auto Load
    ↓
Continue / New Game
    ↓
開始遊戲
    ↓
AUTO_SAVE
```

更多操作請參閱 `07_Documents/SOP/`。

---

# Repository Purpose

本 Repository 為《天下風雲錄》唯一正式 Canon Repository。

主要負責保存與維護：
- Story Bible
- Runtime
- Official Databases
- Gameplay
- Official Patch Notes
- Project Rules
- Documentation
- Templates
- Development Tools
- Archives

Repository 不負責創造 Canon，所有 Canon 皆源自 Story Bible。

---

# Repository Structure

```text
天下風雲錄V3.1.0/
00_Index/
01_StoryBible/
02_Runtime/
02_OfficialPatchNotes/
03_Databases/
04_Gameplay/
06_Archives/
06_ProjectRules/
07_Documents/
07_Staging/
07_Templates/
08_Tools/
09_Archive/
CHANGELOG.md
```

---

# Boot Automation

`00_Index/` contains the repository boot modules.

- `AUTO_LOAD.md` — initializes the repository, loads Canon, Runtime and required databases, and resumes the latest session when applicable.
- `AUTO_SAVE.md` — saves Runtime state, world state, character state and session progress.

---

# SOP

```text
07_Documents/SOP/
├── SOP_INDEX.md
├── 快速開始.md
├── 玩家操作手冊.md
├── AI操作手冊.md
└── Repository維護手冊.md
```

---

# Canon Hierarchy

Story Bible → Runtime → Official Databases → Gameplay → Official Patch Notes → Archives

Story Bible 永遠具有最高 Canon。

---

# Repository Principles

所有正式文件必須：
- Traceable
- Cross Referenced
- Canon Consistent
- UTF-8 Encoding
- zh-TW Markdown

---

# Documentation

- README.md
- CHANGELOG.md
- 07_Documents/SOP/

---

# Version

| Item | Version |
|------|---------|
| Story Bible | v3.1.0 |
| Repository | v3.1.0 |
| Runtime | v3.1.0 |
| Status | Stable |