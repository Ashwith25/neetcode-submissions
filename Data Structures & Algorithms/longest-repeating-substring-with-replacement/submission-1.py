class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0

        hMap = {}
        max_freq = 0

        for r in range(len(s)):
            hMap[s[r]] = hMap.get(s[r], 0) + 1
            max_freq = max(max_freq, hMap[s[r]])
            
            # If current window size - frequency of most frequent character > k,
            # we must shrink the window from the left.
            while (r - l + 1) - max_freq > k:
                hMap[s[l]] -= 1
                l += 1
                # Recalculate max_freq for the current window
                max_freq = max(hMap.values()) if hMap else 0
            
            best = max(best, r - l + 1)

        return best