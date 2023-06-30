class Solution:

    @staticmethod
    def generateParenthesis(n: int) -> list[str]:

        stack = []
        result = []

        def backtrack(abertos, fechados):
            if abertos == fechados == n:
                result.append("".join(stack))
                return

            if abertos < n:
                stack.append('(')
                backtrack(abertos + 1, fechados)
                stack.pop()

            if abertos > fechados:
                stack.append(')')
                backtrack(abertos, fechados + 1)
                stack.pop()

        backtrack(0, 0)
        return result


print(Solution.generateParenthesis(3))
