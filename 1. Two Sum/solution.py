class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 2:
            return [0,1]
        
        for ii in range(len(nums)):
            for jj in range(len(nums)):
            
                if ii == jj:
                    continue
                elif nums[ii] + nums[jj] == target:
                    return [ii,jj]