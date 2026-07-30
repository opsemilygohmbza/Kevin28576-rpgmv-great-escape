# RPG Maker MV 全員逃走中

> ⚠️ 本專案已封存，不再維護。

## 專案時間

最後更新：2023 年 12 月

## 專案簡介

這是一個使用 RPG Maker MV 引擎製作的小遊戲專案，主題參考「全員逃走中」（大逃脫）的遊戲形式。專案內附帶一支 Python 爬蟲腳本，用於搜尋並抓取地圖素材（Google 圖片搜尋結果）以輔助地圖美術製作。

## 內容概覽

- `全員逃走中/`：RPG Maker MV 專案本體
  - `Game.rpgproject`：RPG Maker 專案檔
  - `data/`：遊戲資料（地圖、角色、事件、道具等 JSON 設定）
  - `img/`、`audio/`、`fonts/`、`movies/`、`icon/`：遊戲美術、音效、字型與影片素材
  - `js/`：RPG Maker MV 引擎與外掛程式碼
  - `index.html`：遊戲執行入口
  - `package.json`：NW.js 執行環境設定
- `bug.py`：輔助用 Python 腳本，透過 requests + BeautifulSoup 爬取 Google 圖片搜尋結果，用於尋找地圖素材參考
- `google_search_results.html`：`bug.py` 爬蟲產生的搜尋結果快取頁面

## 備註

- 本專案為 RPG Maker MV 專案，需使用 RPG Maker MV 編輯器或 NW.js 執行環境開啟 `index.html` 才能遊玩。
- `bug.py` 為輔助素材搜尋用的一次性腳本，非遊戲主體程式碼，執行前須自行安裝 `requests`、`beautifulsoup4` 套件。
- 本專案為舊專案封存，僅作備份保存，不再進行後續開發或除錯。
