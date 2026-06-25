class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(currCandidates, i):
            if sum(currCandidates) == target:
                res.append(list(currCandidates))
                return
            if sum(currCandidates) > target or i >= len(candidates):
                return
            
            currCandidates.append(candidates[i])
            dfs(currCandidates, i + 1)

            currCandidates.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(currCandidates, i + 1)

        dfs([], 0)

        return res 