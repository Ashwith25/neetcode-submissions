class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = {}
        
        for i in arr:
            map[i] = map.get(i, 0) + 1

        res = -1

        for k,v in map.items():
            if k==v:
                res = max(res, k)

        return res