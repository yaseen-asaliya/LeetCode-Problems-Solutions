class Solution(object):
    def reverseString(self, s):
        s_len = len(s)

        for index in range(s_len / 2):
            temp = s[index]
            s[index] = s[s_len - 1 - index]
            s[s_len - 1 - index] = temp
        
        return s

        