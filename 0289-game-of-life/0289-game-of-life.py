class Solution:
    def isValidIndex(self, board, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols and (board[r][c] == 1 or board[r][c] == 2)

    def numberOfLiveNeighbors(self, board, r, c, rows, cols):
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        return sum(self.isValidIndex(board, r+dr, c+dc, rows, cols) for dr, dc in directions)

    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live_neighbors = self.numberOfLiveNeighbors(board, r, c, rows, cols)
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2 
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
