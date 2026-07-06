class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        squares = defaultdict(set)

        for rowIndex, rows in enumerate(board):
            rowSet = set()
            for colIndex, cell in enumerate(rows):
                if cell == ".":
                    continue
                
                if int(cell) < 1 or int(cell) > 9:
                    return False
                
                if cell in rowSet:
                    return False
                rowSet.add(cell)

                if cell in cols[colIndex]:
                    return False
                cols[colIndex].add(cell)

                squareIndex = (rowIndex // 3, colIndex // 3)
                if cell in squares[squareIndex]:
                    return False
                squares[squareIndex].add(cell)
        
        return True

