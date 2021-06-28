class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            currentRow = []
            for item in row:
                if item != '.':
                    currentRow.append(int(item))
                    
            if len(currentRow) != len(set(currentRow)):
                return False
            
        # column
        for i in range(9):
            currentColumn = []
            for j in range(9):
                if board[j][i] != '.':
                    currentColumn.append(int(board[j][i]))
                    
            if len(currentColumn) != len(set(currentColumn)):
                return False
            
        # 3x3
        for i in range(3):
            for j in range(3):
                currentSquare = []
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != '.':
                            currentSquare.append(int(board[i * 3 + k][j * 3 + l]))
                
                if len(currentSquare) != len(set(currentSquare)):
                    return False
            
        return True