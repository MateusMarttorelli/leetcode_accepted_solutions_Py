class Solution:
    @staticmethod
    def twoSum(numbers: list[int], target: int) -> list[int]:
        hashmap = dict()

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i


# Test
print(Solution.twoSum([2, 7, 11, 15], 9))
