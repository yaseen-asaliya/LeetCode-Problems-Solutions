class Solution:
    def findComplement(self, num: int) -> int:
        
        temp = list(str(bin(num)[2:]))
        print(temp)
        for index in range(len(temp)):
            if temp[index] == '1':
                temp[index] = '0'
            else:
                temp[index] = '1'

        return int("".join(temp), 2)
