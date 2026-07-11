class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens:
            try:
                converted_num = int(character)
                stack.append(converted_num)
                continue
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                if character == "+":
                    # print(a+b)
                    stack.append(a+b)
                elif character == "-":
                    # print(a-b)
                    stack.append(a-b)
                elif character == "*":
                    # print(a*b)
                    stack.append(a*b)
                else:
                    # print(f"{a}  & {b}")
                    stack.append(int(a/b))
        return stack[-1]
