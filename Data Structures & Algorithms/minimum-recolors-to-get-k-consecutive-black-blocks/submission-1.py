class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        j = 0
        i = 0
        count = 0
        while j<k:
            if blocks[j]=='W':
                count+=1
            j+=1

        tempCount = count
        while j<len(blocks):
            if blocks[i] == 'W':
                tempCount -= 1
            if blocks[j] == 'W':
                tempCount += 1
            
            i+=1
            j+=1
            count = min(count, tempCount)

        return count