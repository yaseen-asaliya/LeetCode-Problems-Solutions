class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if str(x) in str(n) and str(n)[0] != str(x):
            return True
        return False
