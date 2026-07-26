class Solution:
    def decodeString(self, s: str) -> str:
        repeat_stack = []
        string_stack = []
        i=0
        opening = set({'[', '(', '{'})
        closing = set({']', ')', '}'})
        numeric_pointer = 0
        string = ""

        for idx, i in enumerate(s):
            
            if i in opening or i in closing:
                # print(string_stack)
                # print(repeat_stack)
                # print(string)
                # print("****")
                if i in opening:
                    number = int(s[numeric_pointer:idx])
                    repeat_stack.append(number)
                    string_stack.append(string)
                    string = ""
                else:
                    number = repeat_stack.pop()
                    old_string = string_stack.pop()
                    string = old_string + (string*number)

            elif idx>0 and i.isnumeric() and not s[idx-1].isnumeric():
                numeric_pointer = idx
            else:
                if not i.isnumeric(): string += i
        
        string_stack.append(string)

        return "".join(string_stack)

        