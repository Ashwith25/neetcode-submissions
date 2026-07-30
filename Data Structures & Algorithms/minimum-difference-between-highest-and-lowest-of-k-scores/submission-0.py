class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        globalMin = float('inf')

        i=0

        while i<len(nums)-k+1:
            j = i+k-1
            # print(i, j, nums[i], nums[j])
            globalMin = min(globalMin, nums[j]-nums[i])
            i+=1

        return globalMin