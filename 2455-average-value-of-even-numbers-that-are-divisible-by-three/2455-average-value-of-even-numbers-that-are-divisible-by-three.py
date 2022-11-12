class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum,count=0,0
        for i in nums:
            if i%6==0:
                sum+=i
                count+=1
                
        if count!=0:
            return (sum//count)
        else:
            return 0