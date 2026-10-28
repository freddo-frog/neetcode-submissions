class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = "".join([char.lower() for char in s if char.isalnum()])
        rev =  newstr[::-1]

        if rev == newstr:
            return True

        return False    