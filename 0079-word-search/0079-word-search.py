class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                visited[r][c] or board[r][c] != word[index]):
                return False
            
            visited[r][c] = True
            result = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )
            visited[r][c] = False  
            return result

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True

        return False