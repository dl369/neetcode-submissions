class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        maxHeap = []
        result = []

        while r < len(nums):
            # 1. Push the current element into the heap
            heapq.heappush(maxHeap, (-nums[r], r))

            # 2. Once our window reaches the required size 'k'
            if r - l + 1 == k:
                # Lazy deletion: remove elements from the top if they are out of bounds
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                
                # The top of the heap is guaranteed to be the max of the current window
                result.append(-maxHeap[0][0])
                
                # Slide the left pointer forward to maintain window size k for the next iteration
                l += 1
            
            # Slide the right pointer forward
            r += 1

        return result