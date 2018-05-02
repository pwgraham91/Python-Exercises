"""
Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from one
purchase and one sale of one share of Apple stock yesterday.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# Returns 6 (buying for $5 and selling for $11)
"""


def find_max_profit(stock_prices):
    """
    n^2
    """
    max_profit = None
    for iterator_a, a in enumerate(stock_prices):
        for iterator_b in range(len(stock_prices) - iterator_a - 1):
            b = stock_prices[iterator_b + iterator_a + 1]
            profit = b - a
            if max_profit is None or profit > max_profit:
                max_profit = profit
    return max_profit


assert find_max_profit([10, 7, 5, 8, 11, 9]) == 6
assert find_max_profit([10, 7, 5]) == -2


def find_max_profit_optimized(stock_prices):
    min_price = None
    max_profit = None

    for price in stock_prices:
        prev_min_price = min_price
        if min_price is None or price < min_price:
            min_price = price

        profit = None
        if price == min_price:
            if prev_min_price is not None:
                # can't buy and sell in the same minute
                profit = price - prev_min_price
        else:
            profit = price - min_price
        if profit is not None and (max_profit is None or profit > max_profit):
            max_profit = profit
    return max_profit


# assert find_max_profit_optimized([10, 7, 5, 8, 11, 9]) == 6
assert find_max_profit_optimized([10, 7, 5]) == -2

