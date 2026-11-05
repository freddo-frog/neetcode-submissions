class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}   #create hashmap
        for i, n in enumerate(nums):
            need = target - n #find difference store in var
            if need in hashmap:
                return [hashmap[need], i]
            hashmap[n] = i
        return -1
        #loop through and look up
        #return index