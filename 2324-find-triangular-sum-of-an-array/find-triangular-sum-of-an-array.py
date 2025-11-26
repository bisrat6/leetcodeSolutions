from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Continue until the array has just one element
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]
