class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)

        for i in t:
            if len(s) == 0: return True
            if i == s[0]:
                del s[0]

        return len(s) == 0