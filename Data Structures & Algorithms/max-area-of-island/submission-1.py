class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def visit(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + visit(i + 1, j) + visit(i - 1, j) + visit(i, j + 1) + visit(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(visit(i, j), maxArea)
        
        return maxArea