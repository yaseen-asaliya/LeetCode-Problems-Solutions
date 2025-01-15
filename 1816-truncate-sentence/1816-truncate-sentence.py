class Solution(object):
    def truncateSentence(self, s, k):    
        data = s.split(' ')
        res = ""

        for index in range(k):
            res+= data[index]
            if not k - index == 1:
                res+=" "

        return res

        