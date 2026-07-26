class Solution:
    def decodeString(self, s: str) -> str:
        repeat_stack = []
        string_stack = []
        i=0
        opening = set({'[', '(', '{'})
        closing = set({']', ')', '}'})
        string = ""
        number = 0

        for idx, i in enumerate(s):
            if i.isnumeric():
                number = number * 10 + int(i)
            elif i == '[':
                repeat_stack.append(number)
                string_stack.append(string)
                string = ""
                number = 0
            elif i == ']':
                num = repeat_stack.pop()
                old_string = string_stack.pop()
                string = old_string + (string*num)
            else:
                string += i
        
        string_stack.append(string)

        return "".join(string_stack)

        