class Solution(object):
    def minDeletionSize(self, strs):
        if not strs:
            return 0
        
        num_columns = len(strs[0])
        num_columns_to_delete = 0

        for i in range(num_columns):
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] < curr_char:
                    num_columns_to_delete += 1
                    break
                curr_char = strs[j][i]

        return num_columns_to_delete
        