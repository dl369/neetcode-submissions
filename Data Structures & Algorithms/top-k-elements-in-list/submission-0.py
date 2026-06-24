class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1
        
        heap = []
        counter = 0
        for key, val in count.items():
            heapq.heappush(heap, (-val, key, counter))
            counter += 1
        
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result