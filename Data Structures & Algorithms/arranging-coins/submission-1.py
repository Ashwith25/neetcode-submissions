class Solution:
    def arrangeCoins(self, n: int) -> int:
        def feasibility(steps):
            return ((steps * (steps+1)) / 2) <= n

        i=0
        j=n

        best = 0

        while i<=j:
            mid = i + (j-i)//2

            if not feasibility(mid):
                j = mid-1
            else:
                best = mid
                i = mid+1

        return best