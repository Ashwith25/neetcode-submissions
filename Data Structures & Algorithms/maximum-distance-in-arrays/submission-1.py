class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1]

        maxDist = 0

        for i in arrays[1:]:
            maxLocalDist = max(abs(i[-1] - globalMin), abs(globalMax - i[0]))
            # print(maxLocalDist, maxDist, globalMin, globalMax)
            maxDist = max(maxDist, maxLocalDist)

            globalMin = min(globalMin, i[0])
            globalMax = max(globalMax, i[-1])


        return maxDist