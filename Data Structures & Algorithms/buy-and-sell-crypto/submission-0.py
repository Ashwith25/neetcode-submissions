class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        best = 0
        for i in prices[1:]:
            best = max(best, i-left)
            left = min(left, i)

        return best