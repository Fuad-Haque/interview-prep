# Best Time to Buy and Sell Stock — maximize profit from a single buy/sell pair.

# brute force method

def max_profit(prices):
    best = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > best:
                best = profit
    return best

print(max_profit([7, 1, 5, 3, 6, 4]))


