class Solution(object):
    def findTheDifference(self, s, t):
        for letter in t:
            if s.count(letter) != t.count(letter):
                return letter
            
        