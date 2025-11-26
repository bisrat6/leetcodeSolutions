from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, v in enumerate(nums):
            # right sum = total sum minus left sum minus current element
            if left_sum == total - left_sum - v:
                return i
            left_sum += v
        
        return -1
