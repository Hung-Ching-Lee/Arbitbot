# Arbitbot - 加密貨幣跨交易所套利機器人

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7+-blue)

## 📌 功能介紹

Arbitbot 是一個輕量級的加密貨幣跨交易所套利檢測機器人，主要功能包括：

- 🔍 **多交易所價格監控** - 使用 CCXT 庫實時獲取多個交易所的價格
- 💹 **自動套利檢測** - 自動識別價差大於設定閾值的套利機會
- 📢 **Telegram 即時通知** - 發現機會立即推送到 Telegram
- 📊 **詳細日誌記錄** - 完整的操作和交易記錄
- ⚙️ **靈活配置** - 易於配置的 YAML 配置文件

## 🚀 快速開始

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 配置

1. 複製配置模板：
```bash
cp config/config.example.yaml config/config.yaml
```

2. 編輯 `config/config.yaml` 並填入你的信息：
   - Telegram Bot Token 和 Chat ID
   - 交易所名稱
   - 監控的交易對
   - 利潤閾值

### 運行

```bash
python main.py
```

## 📋 配置說明

### config.yaml

```yaml
exchanges:
  exchange1: binance      # 交易所1
  exchange2: bybit        # 交易所2

telegram:
  token: "YOUR_TOKEN"     # Telegram Bot Token
  chat_id: "YOUR_CHAT_ID" # 接收通知的 Chat ID

arbitrage:
  profit_threshold: 0.5   # 利潤閾值（百分比）
  symbols:                # 監控的交易對
    - BTC/USDT
    - ETH/USDT
  check_interval: 60      # 檢查間隔（秒）
```

## 🔧 模組說明

| 模組 | 功能 |
|------|------|
| `arbitbot.config` | 配置管理 |
| `arbitbot.fetcher` | CCXT 數據獲取 |
| `arbitbot.arbitrage` | 套利檢測和計算 |
| `arbitbot.notifier` | Telegram 通知 |
| `arbitbot.utils` | 工具函數 |

## 📦 PyPI 發佈

### 1. 安裝打包工具

```bash
pip install build twine
```

### 2. 構建包

```bash
python -m build
```

### 3. 上傳到 PyPI

```bash
twine upload dist/*
```

> 需要在 PyPI 註冊帳號並配置 `~/.pypirc`

## 🐙 GitHub 發佈

### 1. 初始化 Git 倉庫

```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. 推送到 GitHub

```bash
git remote add origin https://github.com/yourusername/arbitbot.git
git branch -M main
git push -u origin main
```

### 3. 創建 Release

在 GitHub 上創建 Release 標籤，自動觸發 CI/CD 流程

## 📝 使用示例

```python
from arbitbot import ArbitrageBot, TelegramNotifier
from arbitbot.config import Config

# 加載配置
config = Config('config/config.yaml')

# 初始化機器人
bot = ArbitrageBot(
    exchanges=['binance', 'bybit'],
    profit_threshold=0.5
)

# 尋找套利機會
opportunities = bot.find_opportunities(['BTC/USDT', 'ETH/USDT'])

# 發送通知
notifier = TelegramNotifier(config.get('telegram.token'),
                           config.get('telegram.chat_id'))
notifier.notify_opportunities(opportunities)
```

## 🧪 測試

```bash
pytest tests/
```

## 📄 License

MIT License - 詳見 [LICENSE](LICENSE)

## ⚠️ 免責聲明

本工具僅供教育和研究用途。使用者應自行承擔使用本工具進行交易的所有風險和損失。作者不承擔任何法律責任。

## 👨‍💻 貢獻

歡迎提交 Issue 和 Pull Request！

## 📧 聯繫方式

如有問題，請通過 GitHub Issues 聯繫。
