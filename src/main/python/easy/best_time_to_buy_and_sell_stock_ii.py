# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


# author li.hzh
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) <= 1:
            return 0
        buy = sell = prices[0]
        profit = 0
        for index in range(1, len(prices)):
            if prices[index] < sell:
                profit += (sell - buy)
                buy = sell = prices[++index]
            else:
                sell = prices[index]
        profit += (sell - buy)
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 6, 7, 3, 5]))
