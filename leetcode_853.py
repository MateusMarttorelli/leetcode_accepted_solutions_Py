class Solution:

    @staticmethod
    def carFleet(target: int, position: list[int], speed: list[int]) -> int:

        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(cars, reverse=True):
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


print(Solution.carFleet(100, [0, 2, 4], [4, 2, 1]))
