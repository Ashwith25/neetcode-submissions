class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=1

        while j<len(nums):
            while i<j and nums[i]%2==0:
                i+=1
            if nums[j]%2==0:
                nums[i], nums[j] = nums[j], nums[i]

            j+=1

        return nums
