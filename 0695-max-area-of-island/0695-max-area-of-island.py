class Solution:
    def calculateArea(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0

        grid[row][col] = 0

        area = 1

        area += self.calculateArea(grid, row + 1, col)
        area += self.calculateArea(grid, row - 1, col)
        area += self.calculateArea(grid, row, col + 1)
        area += self.calculateArea(grid, row, col - 1)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    current_area = self.calculateArea(grid, row, col)
                    max_area = max(max_area, current_area)

        return max_area