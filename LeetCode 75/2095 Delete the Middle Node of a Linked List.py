# 2095. Delete the Middle Node of a Linked List

# Hint
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

# Example 1:

# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 

# Example 2:

# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# Example 3:

# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
 
# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head):
        fast = slow = head
        prev_slow = None

        # Traverse the list using two pointers, where one moves two steps at a time and the other moves one step at a time.
        # When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        if prev_slow:
            # If the previous of the slow pointer is not None, then the slow pointer is not the head of the list.
            # In this case, we can remove the middle node by updating the next pointer of the previous node of the slow pointer.
            prev_slow.next = slow.next
        else:
            head = head.next

        return head 