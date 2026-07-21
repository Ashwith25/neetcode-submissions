class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = left + (right - left)//2
            print(f"left: {left}, num[left]: {nums[left]}, right: {right}, num[right]: {nums[right]}, mid: {mid} num[mid]: {nums[mid]}", end="\n********\n")
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1