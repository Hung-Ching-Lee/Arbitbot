# 📖 Arbitbot 使用指南

## 🚀 兩個主要功能

### ✨ 功能 1: 在 Jupyter 中使用 GUI 界面（推薦）

**優點:**
- 🎨 圖形化界面，操作簡單
- 📊 實時顯示結果表格
- ⚙️ 支持動態配置
- 🛑 隨時停止檢測

**步驟:**

1. **打開 Notebook**
   ```bash
   jupyter notebook Arbitbot_Interactive.ipynb
   ```

2. **運行所有單元格** (Shift + Enter)
   - 單元格 1-3: 安裝依賴和導入庫
   - 單元格 4-5: 定義核心功能
   - 單元格 6-9: 配置 GUI 和事件處理
   - 單元格 10: 啟動 GUI

3. **配置參數**
   - 🏢 選擇交易所（Binance、Bybit 等）
   - 💱 輸入交易對（BTC/USDT、ETH/USDT）
   - 💰 設置利潤閾值（%)

4. **可選：啟用 Telegram**
   - ✅ 勾選 "啟用 Telegram 推送"
   - 🔑 輸入 Bot Token
   - 💬 輸入 Chat ID

5. **點擊 "🚀 開始檢測"**
   - 實時監控開始
   - 發現機會立即通知

6. **點擊 "⏹ 停止" 終止**

### ✨ 功能 2: 命令行模式（自動化）

**優點:**
- 🤖 自動化部署
- 📝 可選 Telegram 推送
- 🔄 持續運行

**步驟:**

1. **配置環境變數**
   ```bash
   export EXCHANGE1=binance
   export EXCHANGE2=bybit
   export PROFIT_THRESHOLD=0.5
   export SYMBOLS="BTC/USDT,ETH/USDT"
   
   # 可選：Telegram 配置
   export TELEGRAM_TOKEN="your_token"
   export TELEGRAM_CHAT_ID="your_chat_id"
   ```

2. **運行主程式**
   ```bash
   python main.py
   ```

---

## 🔧 配置說明

### Jupyter GUI 參數

| 參數 | 說明 | 範例 |
|------|------|------|
| 交易所 | 監控的交易所 | binance, bybit, okx |
| 交易對 | 檢測的交易對 | BTC/USDT, ETH/USDT |
| 利潤閾值 | 最小利潤% | 0.5 |
| TG Token | Telegram Bot Token | 123456:ABC... |
| TG Chat ID | 接收通知的 Chat ID | 1234567890 |

### 配置文件 (config.yaml)

```yaml
exchanges:
  exchange1: binance
  exchange2: bybit

telegram:
  token: "YOUR_TOKEN"
  chat_id: "YOUR_CHAT_ID"

arbitrage:
  profit_threshold: 0.5
  symbols:
    - BTC/USDT
    - ETH/USDT
  check_interval: 60
```

---

## 📱 獲取 Telegram 配置

### 第 1 步: 創建 Bot
1. 打開 Telegram，搜索 `@BotFather`
2. 發送 `/newbot`
3. 按照提示創建新 Bot
4. 複製得到的 Token（格式: 123456:ABC...）

### 第 2 步: 獲取 Chat ID
1. 搜索 `@userinfobot`
2. 發送任何消息
3. 機器人會返回你的 Chat ID

### 第 3 步: 測試連接
1. 在 Jupyter GUI 中填入 Token 和 Chat ID
2. 啟用 Telegram 推送
3. 開始檢測，第一個結果會推送到 Telegram

---

## 🧪 測試檢測邏輯

```bash
python test_logic.py
```

**測試內容:**
- ✅ 利潤計算公式
- ✅ 機會過濾邏輯
- ✅ 交易所價格對比

---

## 📊 理解結果

### GUI 顯示解讀

| 符號 | 含義 |
|------|------|
| ✅ | 發現套利機會 |
| ℹ️ | 暫未發現機會 |
| ❌ | 出現錯誤 |
| ⏳ | 正在初始化 |

### 結果表格

```
交易對     買入所   賣出所   買價      賣價      利潤(%)
BTC/USDT  binance bybit  30000.00 30150.00 0.50
ETH/USDT  okx     kucoin  1800.50  1812.75  0.68
```

---

## 🚨 常見問題

### Q1: 為什麼沒有發現套利機會？

**A:** 
- 檢查網絡連接
- 確認交易對在所有交易所都存在
- 降低利潤閾值試試
- 不是所有交易對都有套利機會

### Q2: Telegram 消息未收到？

**A:**
- 驗證 Token 和 Chat ID 是否正確
- 確保網絡可以訪問 Telegram API
- 檢查 Bot 是否已添加到聊天中

### Q3: API 速率限制？

**A:**
- 增加檢查間隔 (check_interval)
- 減少監控的交易對數量
- 使用不同的 API key

---

## 💡 優化建議

1. **提高檢測速度**
   - 減少監控的交易對
   - 增加檢查間隔（減少 API 調用）

2. **發現更多機會**
   - 監控更多交易所
   - 降低利潤閾值
   - 監控更多交易對

3. **避免被限流**
   - 不要頻繁切換交易所
   - 使用 API keys 提高限額
   - 合理安排檢查間隔

---

## 📦 依賴包

```txt
ccxt>=2.0              # 交易所 API
ipywidgets>=8.0        # Jupyter GUI
pandas>=1.0            # 數據處理
plotly>=5.0            # 數據可視化
requests>=2.25.0       # HTTP 請求
python-telegram-bot    # Telegram 通知
pyyaml>=5.0            # YAML 配置
```

---

## 🎓 架構說明

### Jupyter Notebook 方案

```
GUI 輸入
  ↓
ArbitrageDetector
  ├─ initialize_exchanges()     # 連接交易所
  ├─ get_price()               # 獲取價格
  └─ find_opportunities()      # 檢測套利
  ↓
結果表格 + Telegram 推送
```

### CLI 方案

```
配置文件/環境變數
  ↓
Main.py
  ├─ Config 加載
  ├─ ArbitrageBot 初始化
  └─ 主循環
  ↓
日誌 + Telegram 推送
```

---

## 📝 License

MIT License

---

## ❓ 需要幫助？

- 📚 查看 README.md
- 🧪 運行 test_logic.py
- 💬 查看代碼註解
