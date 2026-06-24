class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1
        
        heap = []
        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
                
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result