from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(step):
            if step == 0 or step == 1:
                return 0
            
            return min(dfs(step - 1) + cost[step - 1], dfs(step - 2) + cost[step - 2])
        
        return dfs(len(cost))