class Solution(object):
    def luckyNumbers(self, matrix):
        
        row_min = [(min(row), row.index(min(row))) for row in matrix]
    
        col_max = [max(col) for col in zip(*matrix)]
        
        lucky_nums = []
        for value, col_index in row_min:
            if value == col_max[col_index]:
                lucky_nums.append(value)
        
        return lucky_nums
        