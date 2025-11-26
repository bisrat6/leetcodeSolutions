from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                # perform flip on nums[i], nums[i+1], nums[i+2]
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ops += 1
        # after trying flips, check if all are 1
        return ops if nums[-1] == 1 and nums[-2] == 1 else -1
