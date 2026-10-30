class Solution:
    def firstUniqChar(self, s: str) -> int:
        #intialise seen hash map 
        counts = {}
        #loop through string and count each character
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        
        return -1