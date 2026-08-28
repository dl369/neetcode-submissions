# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head

        # Advance fast pointer by n steps
        for _ in range(n):
            fast = fast.next

        # If fast is None, the node to remove is the head itself
        if not fast:
            return head.next

        # Move both until fast is at the last node
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return head