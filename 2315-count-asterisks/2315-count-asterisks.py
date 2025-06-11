class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        is_between = False

        for x in s:
            if x == '|':
                is_between = not is_between  
            elif x == '*' and not is_between:
                count += 1
        
        return count