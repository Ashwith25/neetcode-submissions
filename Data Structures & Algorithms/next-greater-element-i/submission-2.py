class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * (max(nums2)+1)
        stack = []
        for i in nums2:
            if not stack or i<=stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1]<=i:
                    res[stack.pop()] = i
                stack.append(i)

        # print(res)
        return [res[x] for x in nums1]