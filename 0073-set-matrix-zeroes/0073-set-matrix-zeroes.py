class Solution:
    def setZerosRow(self, matrix, res, num_of_col):
        for index in res:
            for i in range(num_of_col):
                matrix[index[0]][i] = 0

    def setZerosCol(self, matrix, res, num_of_row):
        for index in res:
            for i in range(num_of_row):
                matrix[i][index[1]] = 0
                

    def setZeroes(self, matrix: List[List[int]]) -> None:
        res = []
        num_of_row = len(matrix)
        num_of_col = len(matrix[0])

        for row in range(num_of_row):
            for col in range(num_of_col):
                if matrix[row][col] == 0:
                    res.append([row, col])
        print(res)
        self.setZerosRow(matrix, res, num_of_col)
        self.setZerosCol(matrix, res, num_of_row)


            