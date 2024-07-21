# Merge Two Sorted Lists

Problem Description
Merge two sorted linked lists, list1 and list2, into a single sorted list. Merged list should be created by splicing together nodes from both input lists. Return head of merged linked list.

Approach - Merge Sort Technique

* Initialize dummy node as starting point for merged list.
* Maintain a current node that will keep track of appended nodes from list1 and list2.
* While both list1 and list2 have nodes to compare:
---If value of current node in list1 is less than value in list2, append node from list1 to merged list and move to next node in list1.
---Else, append node from list2 to merged list and move to next node in list2.
* After loop, if any nodes remain in list1, append them to merged list.
---Same for any remaining nodes in list2.
* Return merged list starting after dummy node.
