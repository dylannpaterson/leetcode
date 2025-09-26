class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list2ListNode(lst):

        first_node = ListNode(lst[0])
        current_node = first_node
        
        for l in lst[1:]:
            next_node = ListNode(l)
            current_node.next = next_node
            current_node = next_node

        return first_node
    
    def compareLinkedList(l1,l2):

        lists_same = True

        while l1 is not None and l2 is not None:
            lists_same = lists_same and l1.val == l2.val

            l1 = l1.next
            l2 = l2.next

        lists_same = lists_same and l1 is None and l2 is None
        
        return lists_same



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry_over = 0

        first_node = ListNode(0)
        current_node = first_node

        current_node_l1 = l1
        current_node_l2 = l2

        while current_node_l1 is not None or current_node_l2 is not None:

            if current_node_l1 is None:
                current_val_l1 = 0
            else:
                current_val_l1 = current_node_l1.val
                current_node_l1 = current_node_l1.next

            if current_node_l2 is None:
                current_val_l2 = 0
            else:
                current_val_l2 = current_node_l2.val
                current_node_l2 = current_node_l2.next

            digit_sum = current_val_l1 + current_val_l2 + carry_over

            carry_over = int(digit_sum/10)

            digit = digit_sum % 10

            next_node = ListNode(digit)
            current_node.next = next_node
            current_node = current_node.next


        if carry_over > 0:
            next_node = ListNode(carry_over)
            current_node.next = next_node

        return(first_node.next)