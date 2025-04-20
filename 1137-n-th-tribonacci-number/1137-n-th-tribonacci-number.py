class Solution:
    def tribonacci(self, n: int) -> int:
        p1, p2, p3 = 0, 1, 1
        temp = p1+p2+p3

        for x in range(2, n):
            temp = p1+p2+p3
            p1=p2
            p2=p3
            p3=temp
        
        return temp
