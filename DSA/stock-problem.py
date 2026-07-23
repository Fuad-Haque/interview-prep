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


"""At every single day, 
you only need two numbers: the lowest price seen so far, and the best profit seen so far."""


# optimized version

def maxx_profit(pricess):
    """
    Returns the maximum profit from buying and selling once.
    pricess: list of daily stock prices
    """
    min_price = pricess[0]
    best = 0

    for p in pricess:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best

print(maxx_profit([8, 2, 6, 4, 7, 5]))

