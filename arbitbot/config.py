"""
配置管理模組
"""

import os
import yaml
from typing import Dict, Any


class Config:
    """配置管理類"""

    def __init__(self, config_file: str = None):
        """
        初始化配置
        
        Args:
            config_file: YAML 配置文件路徑
        """
        self.config = {}
        if config_file and os.path.exists(config_file):
            self.load_from_file(config_file)
        else:
            self.load_from_env()

    def load_from_file(self, config_file: str):
        """從 YAML 文件加載配置"""
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

    def load_from_env(self):
        """從環境變數加載配置"""
        self.config = {
            'exchanges': {
                'exchange1': os.getenv('EXCHANGE1', 'binance'),
                'exchange2': os.getenv('EXCHANGE2', 'bybit'),
            },
            'telegram': {
                'token': os.getenv('TELEGRAM_TOKEN', ''),
                'chat_id': os.getenv('TELEGRAM_CHAT_ID', ''),
            },
            'arbitrage': {
                'profit_threshold': float(os.getenv('PROFIT_THRESHOLD', '0.5')),
                'symbols': os.getenv('SYMBOLS', 'BTC/USDT,ETH/USDT').split(','),
                'check_interval': int(os.getenv('CHECK_INTERVAL', '60')),
            }
        }

    def get(self, key: str, default: Any = None) -> Any:
        """獲取配置值"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default

    def __repr__(self):
        return f"<Config {self.config}>"
