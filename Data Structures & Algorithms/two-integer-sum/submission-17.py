class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for current_ind, current_num in enumerate(nums):
            complement = target - current_num
            if complement in seen:
                return [seen[complement], current_ind]
            
            seen[current_num] = current_ind
