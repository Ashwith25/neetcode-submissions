class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsSet = [set() for i in range(len(board))]
        colSet = [set() for i in range(len(board[0]))]
        gridSet = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                if not board[i][j].isnumeric():
                    continue
                gridNumber = (i // 3)*3 + (j // 3)
                if board[i][j] in rowsSet[i] or board[i][j] in colSet[j] or board[i][j] in gridSet[gridNumber]:
                    print(i, j, gridNumber, board[i][j])
                    return False
                
                rowsSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                gridSet[gridNumber].add(board[i][j])

        return True