# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()

        for l in lists:
            if l is not None:
                heapq.heappush(heap, NodeWrapper(l))
        
        curr = dummy

        while heap:
            smallest = heapq.heappop(heap).node
            curr.next = smallest
            curr = curr.next
        
            if smallest.next:
                heapq.heappush(heap, NodeWrapper(smallest.next))

        return dummy.next