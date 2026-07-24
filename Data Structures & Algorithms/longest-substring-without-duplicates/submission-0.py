class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = {}
        best = 0

        for r in range(len(s)):
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
            chars[s[r]] = r
            best = max(best, r-l+1)

        return best