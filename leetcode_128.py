class Solution:
    @staticmethod
    def longestConsecutive(nums: list[int]) -> int:

        hashset = set(nums)
        maior_sequencia = 0

        for n in nums:

            if (n - 1) not in hashset:
                aux = 0

                while n + aux in hashset:
                    aux += 1

                if aux > maior_sequencia:
                    maior_sequencia = aux

        return maior_sequencia
