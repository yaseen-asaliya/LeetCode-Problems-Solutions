class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        row_dict = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_dict:
                row_dict[row_tuple] += 1
            else:
                row_dict[row_tuple] = 1

        count = 0
        for j in range(n):
            col_tuple = tuple(grid[i][j] for i in range(n))
            if col_tuple in row_dict:
                count += row_dict[col_tuple]  

        return count