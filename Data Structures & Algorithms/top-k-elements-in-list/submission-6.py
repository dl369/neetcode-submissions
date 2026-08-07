class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for l in reversed(freq):
            for num in l:
                res.append(num)
                if len(res) == k:
                    return res