class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        // backtracking algo

        solve(board); 
    }

    bool solve(vector<vector<char>>& board) {
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                if(board[i][j] == '.'){
                    for(char c = '1'; c <= '9'; c++){//trial. Try 1 through 9
                        if(isValid(board, i, j, c)){
                            board[i][j] = c; //Put c for this cell
                            
                            if(solve(board))
                                return true; //If it's the solution return true
                            else
                                board[i][j] = '.'; //Otherwise go back
                        }
                    }
                    
                    return false;
                }
            }
        }
        return true;
    }

    bool isValid(vector<vector<char>>& board, int row, int col, char c) {
        for(int i = 0; i < 9; i++) {
            if(board[i][col] != '.' && board[i][col] == c) return false; //check row
            if(board[row][i] != '.' && board[row][i] == c) return false; //check column
            if(board[3 * (row / 3) + i / 3][ 3 * (col / 3) + i % 3] != '.' && 
board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false; //check 3*3 block
        }
        return true;
    }
};


// # py solution too slow :(
// # class Solution:
// #     def solveSudoku(self, board: List[List[str]]) -> None:
// #         """
// #         Do not return anything, modify board in-place instead.
// #         """
// #         # backtracking algo
// #         self.board = board
// #         self.solve()
    
// #     def solve(self):
// #         for i in range(9):
// #             for j in range(9):
// #                 if self.board[i][j] == '.':
// #                     for k in range(9):
// #                         if self.checkValid(i, j, str(k + 1)):
// #                             self.board[i][j] = str(k + 1)
// #                         if self.solve():
// #                             return True
// #                         else:
// #                             # reset state
// #                             self.board[i][j] = '.'

// #                     return False
// #         return True

// #     def checkValid(self, row: int, col: int, num: str) -> bool:
// #         # check row and column
// #         for i in range(9):
// #             if (self.board[i][col] == num and self.board[i][col] != '.'):
// #                 return False
// #             if (self.board[row][i] == num and self.board[row][i] != '.'):
// #                 return False
// #             if self.board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num and self.board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.':
// #                 return False
