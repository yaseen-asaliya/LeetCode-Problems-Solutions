class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        dic = {}

        for item in items1:
            dic[item[0]] = dic.get(item[0], 0) + item[1]
        
        for item in items2:
            dic[item[0]] = dic.get(item[0], 0) + item[1]
        
        sorted_items = sorted(dic.items())  

        ret = [[key, value] for key, value in sorted_items]
        
        return ret
        