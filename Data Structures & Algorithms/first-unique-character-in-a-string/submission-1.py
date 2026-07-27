class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0]*26

        for i in s:
            index = ord(i) - ord('a')
            chars[index] += 1

        for idx, char in enumerate(s):
            index = ord(char) - ord('a')
            if chars[index]==1:
                return idx

        return -1