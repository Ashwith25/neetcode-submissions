class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        for idx, i in enumerate(temperatures):
            if stack and temperatures[stack[-1]] > i:
                stack.append(idx)
            else:
                while stack and temperatures[stack[-1]] < i:
                    index = stack.pop()
                    res[index] = idx - index
            stack.append(idx)

        return res