class Solution:

    @staticmethod
    def evalRPN(tokens: list[str]) -> int:

        valid_operators = ['+', '-', '*', '/']
        stack = list()

        for x in tokens:
            if x in valid_operators:
                if x == '+':
                    stack.append(stack.pop(-2) + stack.pop(-1))

                elif x == '-':
                    stack.append(stack.pop(-2) - stack.pop(-1))

                elif x == '*':
                    stack.append(stack.pop(-2) * stack.pop(-1))

                elif x == '/':
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(x))

        return stack[0]
