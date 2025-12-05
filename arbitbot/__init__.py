"""
Arbitbot - 加密貨幣跨交易所套利機器人
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .arbitrage import ArbitrageBot
from .fetcher import PriceFetcher
from .notifier import TelegramNotifier

__all__ = ["ArbitrageBot", "PriceFetcher", "TelegramNotifier"]
