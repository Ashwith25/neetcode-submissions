class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = [0]*26

        for i in magazine:
            index = ord(i) - ord('a')
            chars[index] += 1

        for i in ransomNote:
            index = ord(i) - ord('a')
            if chars[index] < 1:
                return False

            chars[index] -= 1
        return True