class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        print(s)
        while i<len(s):
            if s[i].isnumeric():
                j=i
                while s[i].isnumeric():
                    i+=1
            number = int(s[j:i])
            i+=1

            res.append(s[i:number+i])
            i+=number

        return res