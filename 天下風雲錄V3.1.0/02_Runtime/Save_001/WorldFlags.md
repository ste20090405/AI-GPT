---
title: 天下風雲錄 Save_001 WorldFlags
save_id: Save_001
status: Active
type: World Flags
language: zh-TW
visibility: System Only
---

# Save_001 / WorldFlags

## 定位

本檔保存 Save_001 的世界旗標與劇情判定狀態。

本檔屬系統層，不應直接以敘事方式揭露給玩家。

---

## 世界旗標

```text
World_Initialized = False
First_Chapter_Started = False
Current_Time_Set = False
Player_Initialized = False
```

## 劇情旗標

```text
Meet_Key_NPC = False
Join_Faction = False
First_Combat_Triggered = False
```

## 系統旗標

```text
Auto_Record_StoryLog = True
Auto_Record_Journal = True
Auto_Record_QuestLog = True
Auto_Record_CharacterMemory = True
Auto_Record_WorldFlags = True
```

---

## 備註

旗標應以最小必要原則建立。不得為尚未進入遊戲流程的劇情預設過多旗標。
