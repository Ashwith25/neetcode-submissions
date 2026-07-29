class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashset = {}

        i = 0
        j=0
        res = 0

        while j <= len(fruits):
            res = max(res, j-i)
            if j==len(fruits):
                # print("Final: ",i, j)
                return max(res, j-i)
            print(i, j, hashset)
            if fruits[j] in hashset:
                hashset[fruits[j]] += 1
            else:
                if len(hashset.keys())==2:
                    # res = max(res, j-i+1)
                    while len(hashset.keys())>1 and i<j:
                        if hashset[fruits[i]]>0:
                            hashset[fruits[i]] -= 1
                        if hashset[fruits[i]]==0:
                            del hashset[fruits[i]]
                        i+=1
                        print("Inside:", hashset)
                hashset[fruits[j]] = 1
            j+=1

        return res
                    