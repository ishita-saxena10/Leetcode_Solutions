class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m=0
        for i in range(k):
            m+=nums[i]
        res=m
        for i in range(k,len(nums)):
            m+=nums[i]-nums[i-k]
            res=max(res,m)
        return res/k