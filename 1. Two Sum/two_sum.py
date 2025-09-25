class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds two numbers in a list that add up to a specific target.

        This method iterates through a list of numbers, and for each number,
        it calculates the complement required to reach the target. It uses a
        dictionary to store the numbers it has already seen and their indices.
        If the complement is found in the dictionary, it means a solution
        has been found, and the indices of the two numbers are returned.

        :param nums: A list of integers.
        :type nums: List[int]
        :param target: The target sum.
        :type target: int
        :return: A list containing the indices of the two numbers that add up to the target.
        :rtype: List[int]
        """
        
        # A dictionary to store the numbers we've seen and their indices.
        # The key is the number, and the value is its index.
        done = {}
        
        # Iterate through the list of numbers with their indices.
        for ii, n in enumerate(nums):
                
            # Calculate the complement needed to reach the target.
            difference = target - n

            # If the complement is in our dictionary, we have found a solution.
            if difference in done:
                # Return the index of the complement and the current number's index.
                return [done[difference],ii]
            else:
                # If the complement is not found, add the current number and its index to the dictionary.
                done[n] = ii