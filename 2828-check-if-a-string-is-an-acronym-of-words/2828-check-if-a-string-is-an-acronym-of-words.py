class Solution(object):
    def isAcronym(self, words, s):
        temp = list(s)
        
        if len(temp) != len(words):
            return False
        for x, y in zip(words, temp):
            if x[0] != y[0]:
                return False
        return True
        