class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:

        phrase = Solution.convertToNonAlphaNumericLowerString(s)
        inveted_phrase = phrase[::-1]

        if phrase == inveted_phrase:
            return True
        else:
            return False

    @staticmethod
    def convertToNonAlphaNumericLowerString(s: str) -> str:
        converted_string = ""
        for letter in s:
            if letter.isalnum():
                converted_string += letter
        return converted_string.lower()
