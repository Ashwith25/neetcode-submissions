class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        l=0
        r=len(nums)-1

        first = -1

        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]>=target:
                if nums[mid] == target: first = mid
                r = mid - 1
            else:
                l = mid + 1

        if first == -1: return False

        check_idx = first + len(nums) // 2

        return check_idx < len(nums) and nums[check_idx] == target

        # return last-first+1 > len(nums)//2

