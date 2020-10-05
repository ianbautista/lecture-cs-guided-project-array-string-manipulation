def buyAndSellStock(prices):
    min_price = min(prices)
    print(min_price)
    for i in range(len(prices)):
        if prices[i] == min_price:
            max_price = max(prices[i:])
            return max_price - min_price


print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
