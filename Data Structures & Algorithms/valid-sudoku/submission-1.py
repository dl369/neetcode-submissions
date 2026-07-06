class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        squares = defaultdict(set)

        for rowIndex, rows in enumerate(board):
            rowSet = set()
            for colIndex, cell in enumerate(rows):
                if cell == ".":
                    continue

                squareIndex = (rowIndex // 3, colIndex // 3)

                if (int(cell) < 1 
                    or int(cell) > 9 
                    or cell in rowSet 
                    or cell in cols[colIndex] 
                    or cell in squares[squareIndex]
                ):
                    return False
                
                rowSet.add(cell)
                cols[colIndex].add(cell)
                squares[squareIndex].add(cell)
        
        return True

