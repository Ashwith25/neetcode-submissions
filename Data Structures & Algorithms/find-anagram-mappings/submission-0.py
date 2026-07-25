class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}

        for idx, i in enumerate(nums2):
            mapping[i] = idx

        return [mapping[x] for x in nums1]