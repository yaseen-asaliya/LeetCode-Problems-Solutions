class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_len = len(code)
        res = [0] * code_len

        if k == 0:
            return res

        for num in range(code_len):
            if k > 0:
                start = num + 1
                end = num + k + 1
                step = 1
            elif k < 0:
                start = num - 1
                end = num - abs(k) - 1
                step = -1

            for index in range(start, end, step):
                if index > code_len - 1:
                    temp_index = abs(code_len - index) 
                    res[num] += code[temp_index] 
                else:
                    res[num] += code[index] 

        return res



