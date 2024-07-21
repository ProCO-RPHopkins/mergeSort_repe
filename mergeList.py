# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # The reference to the next node

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Initialize dummy node to act as a starting point for merged list
        dummy = ListNode(-1)
        # Current node where nodes are appended from list1 and list2
        current = dummy
        
        # While both lists have nodes to compare
        while list1 and list2:
            # If value of node in list1 is less than value in list2
            if list1.val < list2.val:
                # Append node from list1 to merged list
                current.next = list1
                # Move to next node in list1
                list1 = list1.next
            else:
                # Append node from list2 to merged list
                current.next = list2
                # Move to next node in list2
                list2 = list2.next
            # Move to next node in merged list
            current = current.next
        
        # If remaining nodes in list1, append them to merged list
        if list1:
            current.next = list1
        # If remaining nodes in list2, append them to merged list
        elif list2:
            current.next = list2
        
        # Merged list starts after dummy node
        return dummy.next
