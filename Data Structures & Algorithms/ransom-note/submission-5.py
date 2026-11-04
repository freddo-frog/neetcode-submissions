class Solution:
    def canConstruct(self, note: str, magazine: str) -> bool:
        count = [0] * 26
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        
        for c in note:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False
        
        
        return True