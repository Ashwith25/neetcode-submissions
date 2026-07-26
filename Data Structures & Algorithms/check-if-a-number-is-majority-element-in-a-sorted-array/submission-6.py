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

        l=0
        r=len(nums)-1
        last = -1

        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]>target:
                r = mid - 1
            else:
                if nums[mid] == target: last = mid
                l = mid + 1

        return last-first+1 > len(nums)//2

