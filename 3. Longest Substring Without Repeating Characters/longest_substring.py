class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Finds the length of the longest substring without repeating characters.

        :param s: The input string.
        :type s: str
        :return: The length of the longest substring.
        :rtype: int
        """

        # This is the left pointer of the sliding window.
        left_index = 0

        # We initialize max_length to 1, as a single character is the smallest possible longest substring.
        max_length = 1

        # A dictionary to keep track of the characters we have seen and their indices.
        seen_chars = {}

        # If the string is empty, there is no substring, so the length is 0.
        if len(s) == 0:
            return 0

        # If the string has only one character, the longest substring is the string itself.
        if len(s) == 1:
            return 1
        
        # We add the first character to our dictionary of seen characters.
        seen_chars[s[0]] = 0


        # We iterate through the string starting from the second character.
        for right_index in range(1,len(s)):

            # This is the character at the right pointer of our sliding window.
            char = s[right_index]

            # If we have seen this character before and its last occurrence is within our current window...
            if char in seen_chars and seen_chars[char] >= left_index:
                # ...we move the left pointer of the window to the position after the last occurrence.
                left_index = seen_chars[char] + 1

            # We calculate the length of the current substring.
            length = right_index - left_index + 1

            # If the current substring is longer than our max length, we update it.
            if length > max_length:
                max_length = length

            # We update the last seen index of the current character.
            seen_chars[char] = right_index
            

        return max_length