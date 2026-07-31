class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        s.sort()
        g.sort()

        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                j+=1
                i+=1
                count+=1
            else:
                while j<len(s) and s[j]<g[i]:
                    j+=1

        return count