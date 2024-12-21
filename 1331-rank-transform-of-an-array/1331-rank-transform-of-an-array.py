class Solution(object):
    def arrayRankTransform(self, arr):
        rank = 1
        temp_arr = sorted(arr)
        temp_dict = {}

        for index in range(len(temp_arr)):
            if not temp_arr[index] in temp_dict:
                temp_dict[temp_arr[index]] = rank
                rank+=1
            
                
        for index in range(len(arr)):        
            arr[index] = temp_dict[arr[index]]
        
        return arr
