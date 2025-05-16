class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n

        for r, c in indices:
            row[r] += 1
            col[c] += 1

        odd_rows = sum(r % 2 for r in row)
        odd_cols = sum(c % 2 for c in col)

        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols