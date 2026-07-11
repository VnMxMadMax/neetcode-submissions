class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens:
            try:
                converted_num = int(character)
                stack.append(converted_num)
                continue
            except ValueError:
                if character == "+":
                    b = stack.pop()
                    a = stack.pop()
                    print(a+b)
                    stack.append(a+b)
                elif character == "-":
                    b = stack.pop()
                    a = stack.pop()
                    print(a-b)
                    stack.append(a-b)
                elif character == "*":
                    b = stack.pop()
                    a = stack.pop()
                    print(a*b)
                    stack.append(a*b)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    print(f"{a}  & {b}")
                    stack.append(int(a/b))
        return stack[-1]
