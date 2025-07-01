class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        counter = 1

        for index in range(1, len(s)):
            if s[index] == s[index-1]:
                counter += 1 
            else:
                counter = 1

            if counter > 2:
                continue 

            res += s[index]
        
        return res
            



