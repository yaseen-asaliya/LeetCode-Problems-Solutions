class Solution(object):
    def stringMatching(self, words):
        full_str = ' '.join(words)
        res = [i for i in words if full_str.count(i) >= 2]
                
        return res
		
        