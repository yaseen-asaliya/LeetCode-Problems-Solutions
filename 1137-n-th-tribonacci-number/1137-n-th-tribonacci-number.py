class Solution:
    def tribonacci(self, n: int) -> int:
        p1, p2, p3 = 0, 1, 1
        if n < 1: return 0
        if n <= 2: return 1

        for x in range(2, n):
            temp = p1+p2+p3
            p1=p2
            p2=p3
            p3=temp
        
        return temp
