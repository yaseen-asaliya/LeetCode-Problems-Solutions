class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = 2

        while True:
            if num % 2 == 0 and num % n == 0:
                return num
            else:
                num+=1
                