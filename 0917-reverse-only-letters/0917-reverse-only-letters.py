class Solution:
    def isLetter(self, letter: str) -> bool:
        return ('A' <= letter <= 'Z') or ('a' <= letter <= 'z')

    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)  
        p1, p2 = 0, len(s) - 1 
        
        while p1 < p2:
            if not self.isLetter(s[p1]): 
                p1 += 1
            elif not self.isLetter(s[p2]): 
                p2 -= 1
            else:  
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
        
        return ''.join(s)  
