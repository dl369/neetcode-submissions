# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        head = res

        while l1 is not None or l2 is not None:
            if l1 is None:
                sumValues = l2.val + carry
            elif l2 is None:
                sumValues = l1.val + carry
            else:
                sumValues = l1.val + l2.val + carry
            carry = 0

            while sumValues >= 10:
                sumValues -= 10
                carry += 1
            
            head.next = ListNode(sumValues)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            head.next = ListNode(carry)
        
        return res.next









