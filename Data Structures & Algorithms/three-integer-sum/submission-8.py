class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0: return []
        res = []
        L = len(nums)
        for idx, i in enumerate(nums):
            l, r = idx+1, L-1

            if idx > 0 and nums[idx-1]==i:
                continue

            if i>0:
                break

            while l<r:
                summ = nums[l] + nums[r] + i
                if summ<0: l+=1
                elif summ>0: r-=1
                else:
                    res.append([i, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

        return res