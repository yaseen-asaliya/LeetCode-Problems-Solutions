class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        max_num = n * n
        count = [0] * (max_num + 1)  # index 0 unused

        for row in grid:
            for num in row:
                count[num] += 1

        repeated = missing = -1

        for i in range(1, max_num + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i

        return [repeated, missing]