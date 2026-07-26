class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ''
        for i in strs:
            final_string += (str(len(i)) + '#' + i)
        return final_string

    def decode(self, s: str) -> List[str]:
        i = 0
        num = 0
        res = []
        while i<len(s):
            if s[i].isnumeric():
                num = num * 10 + int(s[i])

            elif s[i] == '#':
                res.append(s[i+1:i+num+1])
                i+=num
                num=0
            i+=1

        return res
