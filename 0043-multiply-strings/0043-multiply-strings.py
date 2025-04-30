class Solution:
    def place(self, num):
        if num == 1:
            return num

        res = 1
        for x in range(num-1):
            res*=10
        return res

    def multiply(self, num1: str, num2: str) -> str:
        num1_len = len(num1)
        num2_len = len(num2)

        n1 = 0
        n2 = 0

        for index in range(num1_len):
            n1 += int(num1[index]) * self.place(num1_len-index)
        
        for index in range(num2_len):
            n2 += int(num2[index]) * self.place(num2_len-index)
        
        return str(n1*n2)