class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        temp = []
        for x in words:
            temp.extend([s for s in x.split(separator) if s])  
        return temp


        