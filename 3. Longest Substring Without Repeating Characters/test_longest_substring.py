from longest_substring import Solution

def test_simple_case():
    s = Solution()
    strng = "abcabcbb"
    output = 3
    assert s.lengthOfLongestSubstring(strng) == output

def test_repeated_char_case():
    s = Solution()
    strng = "bbbbb"
    output = 1
    assert s.lengthOfLongestSubstring(strng) == output

def test_subsequence_case():
    s = Solution()
    strng = "pwwkew"
    output = 3
    assert s.lengthOfLongestSubstring(strng) == output

def test_white_space_case():
    s = Solution()
    strng = " "
    output = 1
    assert s.lengthOfLongestSubstring(strng) == output

def test_empty_case():
    s = Solution()
    strng = ""
    output = 0
    assert s.lengthOfLongestSubstring(strng) == output

def test_plaindrome_case():
    s = Solution()
    strng = "abba"
    output = 2
    assert s.lengthOfLongestSubstring(strng) == output

