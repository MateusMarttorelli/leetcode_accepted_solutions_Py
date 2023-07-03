class Solution:

    @staticmethod
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  # pair [temp, index]

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = (i - stack_index)

            stack.append([temp, i])

        return result
