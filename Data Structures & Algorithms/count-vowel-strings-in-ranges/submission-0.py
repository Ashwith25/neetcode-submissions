class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        prefixSum = [0] * (len(words)+1)
        runningSum = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefixSum[i+1] = prefixSum[i] + 1
            else:
                prefixSum[i+1] = prefixSum[i]

        # print(words)
        res = []
        for li, ri in queries:
            res.append(prefixSum[ri+1]-prefixSum[li])

        return res