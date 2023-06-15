class Solution:
    @staticmethod
    def isValid(s: str) -> bool:

        hashmap = {')': '(', '}': '{', ']': '['}
        stack = list()

        for x in s:
            if x in hashmap:
                if stack and stack[-1] == hashmap[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

        if not stack:
            return True
        else:
            return False
