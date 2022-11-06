class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,value in enumerate(nums):
            remaining=target-nums[i]
            if remaining in d:
                return [i,d[remaining]]
            d[value]=i