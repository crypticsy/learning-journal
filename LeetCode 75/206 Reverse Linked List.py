# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 
# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 
# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head):
        output = None
        while head:
            output = ListNode(val=head.val, next=output)
            head = head.next
        return output
    
    def reverseListIterativeOptimal(self, head):
        cur_val, cur_head = None, head
        while cur_head:
            temp = cur_head.next
            cur_head.next = cur_val
            cur_val = cur_head
            cur_head = temp
        return cur_val
    
    def reverseListRecursive(self, head, acc):
        if not head: return acc
        return self.reverseListRecursive(head.next, ListNode(head.val, acc))
    

    def reverseList(self, head):
        # return self.reverseListIterative(head)
        # return self.reverseListIterativeOptimal(head)
        return self.reverseListRecursive(head, None)
        