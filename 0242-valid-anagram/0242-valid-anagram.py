class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        for l1, l2 in zip(s,t):
            if l1 != l2:
                return False

        return True
        