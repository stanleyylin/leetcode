class Solution:    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            self.reveal(board, r, c)
        return board

    
    def reveal(self, board: List[List[str]], r: int, c: int) -> None:
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'E':
            return
        surrounding_mines = self.find_mines(board, r, c, 0)
        if surrounding_mines > 0:
            board[r][c] = str(surrounding_mines)
        else:
            board[r][c] = 'B'
            self.reveal(board, r, c + 1)
            self.reveal(board, r + 1, c + 1)
            self.reveal(board, r + 1, c)
            self.reveal(board, r + 1, c - 1)
            self.reveal(board, r, c - 1)
            self.reveal(board, r - 1, c - 1)
            self.reveal(board, r - 1, c)
            self.reveal(board, r - 1, c + 1)

    def find_mines(self, board: List[List[str]], row: int, col: int, count: int) -> int:
        rows, cols = len(board), len(board[0])
        has_top = row - 1 >= 0
        has_left = col - 1 >= 0
        has_right = col + 1 < cols
        has_bottom = row + 1 < rows

        if has_top and has_right and board[row-1][col+1] == 'M': count += 1
        if has_top and board[row-1][col] == 'M': count += 1
        if has_top and has_left and board[row-1][col-1] == 'M': count += 1
        if has_right and board[row][col+1] == 'M': count += 1
        if has_left and board[row][col-1] == 'M': count += 1
        if has_bottom and has_right and board[row+1][col+1] == 'M': count += 1
        if has_bottom and board[row+1][col] == 'M': count += 1
        if has_bottom and has_left and board[row+1][col-1] == 'M': count += 1
        return count



        