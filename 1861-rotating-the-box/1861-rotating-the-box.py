class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for row in boxGrid:
            empty = n - 1  
            for col in range(n - 1, -1, -1):
                if row[col] == '*':  
                    empty = col - 1
                elif row[col] == '#':  
                    row[col] = '.'
                    row[empty] = '#'
                    empty -= 1

        rotated = [[None] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                rotated[c][m - 1 - r] = boxGrid[r][c]

        return rotated