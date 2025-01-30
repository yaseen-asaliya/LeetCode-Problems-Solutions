class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0

        for row in grid:
            l = len(row)
            for index in range(l, 0, -1):
                if row[index-1] < 0:
                    c+=1

        return c