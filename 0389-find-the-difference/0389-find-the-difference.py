class Solution(object):
    def findTheDifference(self, s, t):
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        s_len = len(s)

        for index in range(s_len):
            if t[index] != s[index]:
                return t[index]
        
        return t[s_len]
            
        