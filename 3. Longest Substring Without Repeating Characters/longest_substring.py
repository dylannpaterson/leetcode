class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left_index = 0

        max_length = 1

        seen_chars = {}

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        seen_chars[s[0]] = 0


        for right_index in range(1,len(s)):

            char = s[right_index]

            if char in seen_chars and seen_chars[char] >= left_index:
                left_index = seen_chars[char] + 1

            length = right_index - left_index + 1

            if length > max_length:
                max_length = length

            seen_chars[char] = right_index
            

        return max_length