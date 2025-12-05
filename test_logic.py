"""
測試套利檢測邏輯和利潤計算
"""

def test_profit_calculation():
    """測試利潤計算公式"""
    
    print("=" * 60)
    print("🧪 測試套利利潤計算")
    print("=" * 60)
    
    # 測試案例1: 基本套利
    buy_price = 30000  # 在交易所 A 買入
    sell_price = 30150  # 在交易所 B 賣出
    profit = ((sell_price - buy_price) / buy_price) * 100
    
    print(f"\n📍 測試 1: 基本套利")
    print(f"  買入價: ${buy_price:.2f}")
    print(f"  賣出價: ${sell_price:.2f}")
    print(f"  利潤: {profit:.4f}%")
    print(f"  預期: 0.5%")
    assert abs(profit - 0.5) < 0.001, f"利潤計算錯誤: 期望 0.5%, 得到 {profit}%"
    print(f"  ✅ 通過")
    
    # 測試案例2: 更大的差價
    buy_price = 1000
    sell_price = 1050
    profit = ((sell_price - buy_price) / buy_price) * 100
    
    print(f"\n📍 測試 2: 5% 利潤")
    print(f"  買入價: ${buy_price:.2f}")
    print(f"  賣出價: ${sell_price:.2f}")
    print(f"  利潤: {profit:.4f}%")
    print(f"  預期: 5.0%")
    assert abs(profit - 5.0) < 0.001, f"利潤計算錯誤: 期望 5.0%, 得到 {profit}%"
    print(f"  ✅ 通過")
    
    # 測試案例3: 無利潤
    buy_price = 100
    sell_price = 100
    profit = ((sell_price - buy_price) / buy_price) * 100
    
    print(f"\n📍 測試 3: 無利潤")
    print(f"  買入價: ${buy_price:.2f}")
    print(f"  賣出價: ${sell_price:.2f}")
    print(f"  利潤: {profit:.4f}%")
    print(f"  預期: 0.0%")
    assert abs(profit - 0.0) < 0.001, f"利潤計算錯誤: 期望 0.0%, 得到 {profit}%"
    print(f"  ✅ 通過")
    
    # 測試案例4: 虧損
    buy_price = 100
    sell_price = 98
    profit = ((sell_price - buy_price) / buy_price) * 100
    
    print(f"\n📍 測試 4: 虧損情況")
    print(f"  買入價: ${buy_price:.2f}")
    print(f"  賣出價: ${sell_price:.2f}")
    print(f"  利潤: {profit:.4f}%")
    print(f"  預期: -2.0%")
    assert abs(profit - (-2.0)) < 0.001, f"利潤計算錯誤: 期望 -2.0%, 得到 {profit}%"
    print(f"  ✅ 通過")
    
    # 測試案例5: ETH 小數位精度
    buy_price = 1800.50
    sell_price = 1812.75
    profit = ((sell_price - buy_price) / buy_price) * 100
    
    print(f"\n📍 測試 5: 浮點數精度")
    print(f"  買入價: ${buy_price:.2f}")
    print(f"  賣出價: ${sell_price:.2f}")
    print(f"  利潤: {profit:.4f}%")
    expected = ((1812.75 - 1800.50) / 1800.50) * 100
    print(f"  預期: {expected:.4f}%")
    assert abs(profit - expected) < 0.0001, f"利潤計算錯誤: 期望 {expected}%, 得到 {profit}%"
    print(f"  ✅ 通過")
    
    print("\n" + "=" * 60)
    print("✅ 所有利潤計算測試通過!")
    print("=" * 60)


def test_opportunity_filtering():
    """測試套利機會過濾邏輯"""
    
    print("\n" + "=" * 60)
    print("🧪 測試套利機會過濾")
    print("=" * 60)
    
    opportunities = [
        {'symbol': 'BTC/USDT', 'profit': 0.3},  # 低於閾值
        {'symbol': 'BTC/USDT', 'profit': 0.5},  # 達到閾值
        {'symbol': 'ETH/USDT', 'profit': 0.8},  # 高於閾值
        {'symbol': 'BNB/USDT', 'profit': -0.1},  # 虧損
    ]
    
    threshold = 0.5
    filtered = [opp for opp in opportunities if opp['profit'] >= threshold]
    
    print(f"\n📍 測試過濾: 閾值 = {threshold}%")
    print(f"  原始機會數: {len(opportunities)}")
    print(f"  過濾後機會數: {len(filtered)}")
    print(f"  期望: 2 個機會")
    
    assert len(filtered) == 2, f"過濾錯誤: 期望 2 個機會，得到 {len(filtered)} 個"
    assert all(opp['profit'] >= threshold for opp in filtered), "過濾邏輯錯誤"
    
    print(f"\n  ✅ 通過")
    print(f"  符合條件的機會:")
    for opp in filtered:
        print(f"    - {opp['symbol']}: {opp['profit']:.2f}%")
    
    print("\n" + "=" * 60)
    print("✅ 所有過濾測試通過!")
    print("=" * 60)


def test_exchange_comparison():
    """測試交易所價格對比邏輯"""
    
    print("\n" + "=" * 60)
    print("🧪 測試交易所價格對比")
    print("=" * 60)
    
    # 模擬來自不同交易所的價格
    prices = {
        'binance': {'ask': 30000, 'bid': 29999},  # ask 是賣出價，bid 是買入價
        'bybit': {'ask': 30100, 'bid': 30099},
        'okx': {'ask': 30050, 'bid': 30049},
    }
    
    print("\n📍 交易所價格數據:")
    for exchange, price in prices.items():
        print(f"  {exchange:10s}: Ask=${price['ask']:.0f} | Bid=${price['bid']:.0f}")
    
    # 找出最低 ask 和最高 bid
    lowest_ask_ex = min(prices.keys(), key=lambda x: prices[x]['ask'])
    highest_bid_ex = max(prices.keys(), key=lambda x: prices[x]['bid'])
    
    lowest_ask = prices[lowest_ask_ex]['ask']
    highest_bid = prices[highest_bid_ex]['bid']
    
    profit = ((highest_bid - lowest_ask) / lowest_ask) * 100
    
    print(f"\n📍 最優套利路徑:")
    print(f"  買入: {lowest_ask_ex} @ ${lowest_ask:.0f}")
    print(f"  賣出: {highest_bid_ex} @ ${highest_bid:.0f}")
    print(f"  利潤: {profit:.4f}%")
    
    assert profit > 0, "應該有正利潤"
    assert lowest_ask_ex == 'binance', f"應該在 binance 買入"
    assert highest_bid_ex == 'bybit', f"應該在 bybit 賣出"
    
    print(f"  ✅ 通過")
    
    print("\n" + "=" * 60)
    print("✅ 所有交易所對比測試通過!")
    print("=" * 60)


if __name__ == '__main__':
    test_profit_calculation()
    test_opportunity_filtering()
    test_exchange_comparison()
    
    print("\n🎉 所有測試完成!")
