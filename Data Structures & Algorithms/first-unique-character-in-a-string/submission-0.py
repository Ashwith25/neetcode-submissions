class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [[0,0] for i in range(26)]

        for idx, i in enumerate(s):
            index = ord(i) - ord('a')
            chars[index] = [idx, chars[index][1]+1]

        for char in s:
            index = ord(char) - ord('a')
            if chars[index][1]==1:
                return chars[index][0]

        return -1