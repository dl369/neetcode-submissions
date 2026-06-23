from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(a):
            if a == 0:
                return 0
            
            return min((dfs(a - x) + 1 for x in coins if a - x >= 0), default=float('inf'))
        
        res = dfs(amount)
        return res if res != float('inf') else -1