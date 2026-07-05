# AUTO_LOAD

本次修訂重點：

- Story Bible (`01_StoryBible/天下風雲錄_Story_Bible_v3.0.3.md`) 為最高 Canon 基礎。
- Boot 時必須載入 Story Bible。
- Boot 時必須接續載入 Official Patch Notes，以 Story Bible 為基礎套用所有官方修正。
- Official Patch Notes 不再限定單一版本檔案名稱，而採版本格式：`天下風雲錄PatchNotes_vX.X.X.md`（X 為數字，例如 `天下風雲錄PatchNotes_v3.0.3.md`、`天下風雲錄PatchNotes_v3.1.0.md`）。
- 若 `02_OfficialPatchNotes/` 內存在多個 PatchNotes 檔案，必須依版本號由低至高依序載入，逐版套用更新，不得跳過任何正式版本。
- 最終 Canon = Story Bible + 全部 Official Patch Notes（依版本順序套用）。
- Runtime、Archive 與後續遊戲內容均以前述最終 Canon 為準，再恢復 Save 狀態並繼續遊戲。

其餘 AUTO_LOAD 流程（Runtime、Archive Sync、Continue Mode、Lazy Loading 等）維持上一版規則不變。