class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

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
