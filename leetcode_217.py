class Solution:
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# Test
print(Solution.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 1]))
