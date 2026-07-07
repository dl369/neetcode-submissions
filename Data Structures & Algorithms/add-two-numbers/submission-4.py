class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        carry = 0

        # Loop continues as long as there are digits to process OR a leftover carry
        while l1 or l2 or carry:
            # Extract values safely, defaulting to 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate total sum and update carry using divmod
            carry, sum_value = divmod(val1 + val2 + carry, 10)

            # Create the next node
            head.next = ListNode(sum_value)
            head = head.next

            # Advance pointers safely
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next