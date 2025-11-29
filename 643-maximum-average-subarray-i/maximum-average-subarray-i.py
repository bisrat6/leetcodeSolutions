class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maximum=summ
        for i in range(k,len(nums)):
            summ+=nums[i]-nums[i-k]
            maximum=max(maximum,summ)
        return maximum/k
