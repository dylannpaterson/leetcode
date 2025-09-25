from add_two import Solution, ListNode

def test_list_compare_simple_case():
    l1 = ListNode.list2ListNode([2,4,3])
    l2 = ListNode.list2ListNode([2,4,3])

    assert ListNode.compareLinkedList(l1,l2)

def test_list_compare_diff_case():
    l1 = ListNode.list2ListNode([2,4,3])
    l2 = ListNode.list2ListNode([2,4])

    assert ListNode.compareLinkedList(l1,l2) == False

def test_list_compare_zeros_case():
    l1 = ListNode.list2ListNode([0])
    l2 = ListNode.list2ListNode([0])

    assert ListNode.compareLinkedList(l1,l2)
    
def test_simple_case():
    s = Solution()
    l1 = ListNode.list2ListNode([2,4,3])
    l2 = ListNode.list2ListNode([5,6,4])
    output = ListNode.list2ListNode([7,0,8])
    assert ListNode.compareLinkedList(s.addTwoNumbers(l1, l2),output)

def test_zeros_case():
    s = Solution()
    l1 = ListNode.list2ListNode([0])
    l2 = ListNode.list2ListNode([0])
    output = ListNode.list2ListNode([0])
    assert ListNode.compareLinkedList(s.addTwoNumbers(l1, l2),output)

def test_diff_digits_l1_longer_case():
    s = Solution()
    l1 = ListNode.list2ListNode([2,4,3])
    l2 = ListNode.list2ListNode([6,4])
    output = ListNode.list2ListNode([8,8,3])
    assert ListNode.compareLinkedList(s.addTwoNumbers(l1, l2),output)

def test_diff_digits_l2_longer_case():
    s = Solution()
    l1 = ListNode.list2ListNode([2,4])
    l2 = ListNode.list2ListNode([6,4,3])
    output = ListNode.list2ListNode([8,8,3])
    assert ListNode.compareLinkedList(s.addTwoNumbers(l1, l2),output)
    
def test_overflow_case():
    s = Solution()
    l1 = ListNode.list2ListNode([9,9,9,9,9])
    l2 = ListNode.list2ListNode([9,9,9,9,9])
    output = ListNode.list2ListNode([8,9,9,9,9,1])
    assert ListNode.compareLinkedList(s.addTwoNumbers(l1, l2),output)