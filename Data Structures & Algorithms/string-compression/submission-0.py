class Solution:
    def compress(self, chars: List[str]) -> int:
        i=k=0
        j=1

        while j<=len(chars):
            if j==len(chars) or chars[j]!=chars[k]:
                chars[i] = chars[k]
                i+=1
                if j-k>1:
                    for x in str(j-k):
                        chars[i] = x
                        i += 1
                k=j
            j+=1

        return i