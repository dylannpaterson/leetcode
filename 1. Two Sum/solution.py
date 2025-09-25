class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 2:
            return [0,1]
        
        done = {}
        
        for ii, n in enumerate(nums):
                
            if ii == 0:
                done[n] = ii
            else:
                difference = target - n

                if difference in done.keys():
                    return [done[difference],ii]
                else:
                   done[n] = ii
