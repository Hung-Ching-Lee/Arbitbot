"""
主程式入口點
"""

import time
import logging
from arbitbot import ArbitrageBot, TelegramNotifier
from arbitbot.config import Config
from arbitbot.utils import setup_logging

# 設置日誌
logger = setup_logging('arbitbot.log')


def main():
    """主程式"""
    
    # 加載配置
    config = Config('config/config.yaml')
    
    logger.info("=" * 50)
    logger.info("🤖 Arbitbot 開始運行")
    logger.info("=" * 50)
    
    # 初始化套利機器人
    exchanges = [
        config.get('exchanges.exchange1'),
        config.get('exchanges.exchange2'),
    ]
    profit_threshold = config.get('arbitrage.profit_threshold', 0.5)
    symbols = config.get('arbitrage.symbols', ['BTC/USDT', 'ETH/USDT'])
    check_interval = config.get('arbitrage.check_interval', 60)
    
    bot = ArbitrageBot(exchanges, profit_threshold)
    
    # 初始化 Telegram 通知器
    telegram_token = config.get('telegram.token', '')
    telegram_chat_id = config.get('telegram.chat_id', '')
    notifier = TelegramNotifier(telegram_token, telegram_chat_id)
    
    logger.info(f"📊 監控交易對: {', '.join(symbols)}")
    logger.info(f"💰 利潤閾值: {profit_threshold}%")
    logger.info(f"⏱️  檢查間隔: {check_interval}秒")
    
    # 主循環
    try:
        iteration = 0
        while True:
            iteration += 1
            logger.info(f"\n--- 第 {iteration} 次掃描 ---")
            
            # 尋找套利機會
            opportunities = bot.find_opportunities(symbols)
            
            if opportunities:
                logger.info(f"✅ 發現 {len(opportunities)} 個套利機會")
                
                # 獲取最優的機會
                best_opps = bot.get_best_opportunities(5)
                for opp in best_opps:
                    logger.info(f"  → {opp}")
                
                # 發送 Telegram 通知
                notifier.notify_opportunities(best_opps)
            else:
                logger.info("ℹ️  未發現套利機會")
            
            # 等待下一次檢查
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        logger.info("\n⏹️  程式已停止")
    except Exception as e:
        logger.error(f"❌ 程式出現異常: {e}", exc_info=True)
        notifier.send_message(f"🚨 <b>Arbitbot 程式異常</b>\n\n{str(e)}")


if __name__ == '__main__':
    main()
