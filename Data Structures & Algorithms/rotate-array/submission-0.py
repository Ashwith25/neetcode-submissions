class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        pivot = k % length

        left = 0
        right = length-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = 0
        right = pivot-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = pivot
        right = length-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

