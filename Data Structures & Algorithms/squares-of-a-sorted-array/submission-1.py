class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [0] * L
        
        idx = L-1

        l = 0
        r = L-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[idx] = nums[l]**2
                l += 1
            else:
                res[idx] = nums[r]**2
                r -= 1
            idx -= 1

        return res