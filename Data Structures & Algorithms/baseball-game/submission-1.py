class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in operations:
            if i=='C':
                top = stack.pop()
                sum -= top
            elif i=='+':
                stack.append(stack[-2] + stack[-1])
                sum += stack[-1]
            elif i=='D':
                stack.append(stack[-1] * 2)
                sum += stack[-1]
            else:
                stack.append(int(i))
                sum += stack[-1]
            # print(sum, stack)
        return sum