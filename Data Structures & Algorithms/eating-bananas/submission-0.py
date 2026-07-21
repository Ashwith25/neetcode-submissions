class Solution:
    def canAchieve(self, piles, k, h):
        hours = 0
        for p in piles:
            hours += (p + k - 1)//k

        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        hi = max(piles)

        while low<hi:
            mid = low + (hi - low) // 2
            if self.canAchieve(piles, mid, h):
                hi = mid
            else:
                low = mid + 1

        return low