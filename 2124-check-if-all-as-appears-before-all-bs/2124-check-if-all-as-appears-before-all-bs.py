class Solution:
    def checkString(self, s: str) -> bool:
        saw_a = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a':
                saw_a = True
            if s[i] == 'b' and saw_a:
                return False
        
        return True