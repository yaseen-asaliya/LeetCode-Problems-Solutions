class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        temp = []
        for x in words:
            splits = x.split(separator) 
            for sp in splits:
                if sp:
                    temp.append(sp)  
        return temp


        