class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        res = [[1],[1,1]]

        for x in range(1, numRows-1):
            t = [1]
            for v in range(len(res[x]) - 1):
                t.append(res[x][v] + res[x][v+1])
            t.append(1)
            res.append(t)

        return res 


