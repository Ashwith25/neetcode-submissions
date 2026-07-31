class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for i in nums2:
            if not stack or i<=stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1]<=i:
                    res[stack.pop()] = i
                stack.append(i)

        # print(res)
        return [res.get(x, -1) for x in nums1]