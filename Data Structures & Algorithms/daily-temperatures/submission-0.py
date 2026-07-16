class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        for idx, i in enumerate(temperatures[1:]):
            idx += 1
            if stack and temperatures[stack[-1]] > i:
                stack.append(idx)
                # print(stack)
            else:
                while stack and temperatures[stack[-1]] < i:
                    index = stack.pop()
                    res[index] = idx - index
                    # print(idx, i)
                    # print("res:", res)
                    # print("stack:", stack)
            stack.append(idx)

        return res