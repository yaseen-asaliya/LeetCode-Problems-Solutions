class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp_res = []
        temp_res_len = 0
        res = 0

        for x in range(len(operations)):
            if operations[x] == 'D':
                temp_res.append(temp_res[temp_res_len-1] * 2)
                temp_res_len+=1
            elif operations[x] == 'C':
                temp_res.pop()
                temp_res_len-=1
            elif operations[x] == '+':
                temp_res.append(temp_res[temp_res_len-1] + temp_res[temp_res_len-2])
                temp_res_len+=1
            else:
                temp_res.append(int(operations[x]))
                temp_res_len+=1

        for x in temp_res:
            res+=x
        return res 
