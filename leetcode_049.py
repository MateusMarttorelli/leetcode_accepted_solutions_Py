class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        res = dict()

        for s in strs:
            key = "".join(sorted(s))

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())


# Test
print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
