class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        hash_frequency = dict()

        for n in nums:
            hash_frequency[n] = hash_frequency.get(n, 0) + 1

        result = list()

        for i in range(k):
            key = max(hash_frequency, key=hash_frequency.get)
            result.append(key)
            hash_frequency.pop(key)

        return result


# Test
print(Solution.topKFrequent([1, 1, 1, 2, 2, 2, 2, 3], 2))
