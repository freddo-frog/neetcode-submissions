class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r  = 0, len(s) - 1

        while l < r: 
            #if  left char is not alnum move pointer in
            while l < r and not s[l].isalnum():
                l += 1
        
            while l < r and not s[r].isalnum():
                #if right char is not alnum move pointer in
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
