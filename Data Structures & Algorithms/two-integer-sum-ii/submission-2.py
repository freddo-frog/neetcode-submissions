class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return[left + 1, right + 1]

            #if sum is too low move left pointer left is +
            elif current_sum < target:
                left += 1
            #if sum is too high move the right one right is -
            else:
                right -= 1

        
