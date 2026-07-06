class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        N = len(grid) - 1

        visited.add((0, 0))

        while minHeap:
            currHeight, i, j = heapq.heappop(minHeap)

            if i == N and j == N:
                return currHeight
            
            for x, y in directions:
                newXCoord = i + x
                newYCoord = j + y
                if ((newXCoord, newYCoord) not in visited 
                    and newXCoord >= 0 
                    and newXCoord <= N 
                    and newYCoord >= 0 
                    and newYCoord <= N
                ):
                    visited.add((newXCoord, newYCoord))
                    newHeight = max(currHeight, grid[newXCoord][newYCoord])
                    heapq.heappush(minHeap, [newHeight, newXCoord, newYCoord])
