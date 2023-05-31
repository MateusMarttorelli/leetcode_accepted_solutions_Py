class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefix, suffix = 1, 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


# Test
print(Solution.productExceptSelf([1, 2, 3, 4]))
