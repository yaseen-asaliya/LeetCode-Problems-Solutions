class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        str_len = len(s)
        c = 0

        for let in s:
            if let == letter:
                c +=1
        
        return int(c / str_len * 100) 