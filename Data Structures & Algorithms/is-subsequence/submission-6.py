class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)

        pointer = 0

        for i in t:
            if len(s) == pointer: return True
            if i == s[pointer]:
                pointer += 1

        return len(s) == pointer