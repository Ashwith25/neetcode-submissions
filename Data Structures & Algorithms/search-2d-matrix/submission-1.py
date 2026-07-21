class Solution:

    def doesExist(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        hi = len(matrix) - 1

        while low <= hi:
            mid = low + (hi - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.doesExist(matrix[mid], target)
                
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                low = mid + 1

        return False