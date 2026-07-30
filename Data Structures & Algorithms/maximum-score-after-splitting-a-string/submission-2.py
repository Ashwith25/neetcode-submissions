class Solution:
    def maxScore(self, s: str) -> int:
        nosOfOne = 0
        for i in s:
            if i=='1':
                nosOfOne+=1

        nosOfZero = 0
        res = 0

        for i in range(len(s)-1):
            if s[i]=='0':
                nosOfZero += 1
            else:
                nosOfOne -= 1

            res = max(res, nosOfZero + nosOfOne)

        return res