from solution import Solution

def test_first_test_case():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    output = [0, 1]
    assert s.twoSum(nums, target) == output

def test_unordered_case():
    s = Solution()
    nums = [3,2,4]
    target = 6
    output = [1, 2]
    assert s.twoSum(nums, target) == output

def test_duplicates_case():
    s = Solution()
    nums = [3,3]
    target = 6
    output = [0, 1]
    assert s.twoSum(nums, target) == output