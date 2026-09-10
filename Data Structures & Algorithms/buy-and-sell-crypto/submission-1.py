class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        i = 0
        j = 1
        maxprofit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                p = prices[j] - prices[i]
                maxprofit = max(maxprofit, p)
            else:
                i = j
            j += 1

        return maxprofit