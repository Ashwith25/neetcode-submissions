class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashset = {}

        i = 0
        j=0
        res = 0

        while j <= len(fruits):
            res = max(res, j-i)
            if j==len(fruits):
                return max(res, j-i)
            hashset[fruits[j]] = hashset.get(fruits[j], 0) + 1
            # if len(hashset.keys())==2:
            while len(hashset.keys())>2 and i<j:
                hashset[fruits[i]] -= 1
                if hashset[fruits[i]]==0:
                    del hashset[fruits[i]]
                i+=1
            # hashset[fruits[j]] = 1
            j+=1

        return res
                    