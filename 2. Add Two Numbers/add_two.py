class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode.

        :param val: The value of the node.
        :param next: The next node in the list.
        """
        self.val = val
        self.next = next

    @staticmethod
    def list2ListNode(lst):
        """
        Converts a Python list to a ListNode linked list.

        :param lst: The list to convert.
        :return: The head of the linked list.
        """
        if not lst:
            return None

        first_node = ListNode(lst[0])
        current_node = first_node
        
        for l in lst[1:]:
            next_node = ListNode(l)
            current_node.next = next_node
            current_node = next_node

        return first_node
    
    @staticmethod
    def compareLinkedList(l1, l2):
        """
        Compares two linked lists to see if they are identical.

        :param l1: The head of the first linked list.
        :param l2: The head of the second linked list.
        :return: True if the lists are the same, False otherwise.
        """
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return l1 is None and l2 is None



class Solution(object):
    """
    Contains the solution for the "Add Two Numbers" problem.
    """
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by linked lists.

        The digits are stored in reverse order, and each of their nodes contains a single digit.
        This function adds the two numbers and returns the sum as a linked list.

        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # To handle any carry-over from adding digits.
        carry_over = 0

        # The first_node is a dummy head. The result will be first_node.next.
        first_node = ListNode(0)
        current_node = first_node

        # Pointers to traverse the input linked lists.
        current_node_l1 = l1
        current_node_l2 = l2

        # Loop until both linked lists are fully traversed.
        while current_node_l1 is not None or current_node_l2 is not None:

            # Get the value of the current node in l1, or 0 if we've reached the end.
            if current_node_l1 is None:
                current_val_l1 = 0
            else:
                current_val_l1 = current_node_l1.val
                current_node_l1 = current_node_l1.next

            # Get the value of the current node in l2, or 0 if we've reached the end.
            if current_node_l2 is None:
                current_val_l2 = 0
            else:
                current_val_l2 = current_node_l2.val
                current_node_l2 = current_node_l2.next

            # Sum the digits and the carry-over.
            digit_sum = current_val_l1 + current_val_l2 + carry_over

            # Calculate the new carry-over for the next iteration.
            carry_over = int(digit_sum/10)

            # The digit for the new node is the remainder of the sum.
            digit = digit_sum % 10

            # Create the new node and append it to our result list.
            next_node = ListNode(digit)
            current_node.next = next_node
            current_node = current_node.next


        # If there's a carry-over after the loop, create a new node for it.
        if carry_over > 0:
            next_node = ListNode(carry_over)
            current_node.next = next_node

        # The result starts from the node after the dummy head.
        return(first_node.next)