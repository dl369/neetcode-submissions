class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1
        
        heap = []
        for key, val in count.items():

            heapq.heappush(heap, (val, key))

            if len(heap) > k:

                heapq.heappop(heap)
                
        return [item[1] for item in heap]