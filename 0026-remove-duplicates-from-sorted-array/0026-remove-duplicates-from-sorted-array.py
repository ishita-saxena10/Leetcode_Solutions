class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        while a != len(nums):
            if nums.count(nums[a]) != 1:
                nums.remove(nums[a])
            else:
                a += 1
        return len(nums)
        