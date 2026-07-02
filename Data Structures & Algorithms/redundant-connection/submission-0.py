class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if n == par[n]:
                return n

            par[n] = find(par[n]) 
            return par[n]
        
        def union(i, j):
            p1, p2 = find(i), find(j)

            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for i, j in edges:
            if not union(i, j):
                return [i, j]
            
        
