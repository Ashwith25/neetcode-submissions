class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []

        def evaluate(num1, num2, operator):
            num1 = int(num1)
            num2 = int(num2)
            if operator == '+':
                return num2+num1
            elif operator == '-':
                return num2-num1
            elif operator == '*':
                return num2*num1
            else:
                return num2/num1

        for i in tokens:
            print(stack)
            if i not in operators: stack.append(i)
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                answer = evaluate(num1, num2, i)
                stack.append(answer)

        return int(stack[-1])
