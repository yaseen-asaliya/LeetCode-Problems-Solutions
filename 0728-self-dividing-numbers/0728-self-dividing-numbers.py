class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        temp = []
        for x in range(left, right + 1):
            st = list(str(x))
            for digit in st:
                if int(digit) != 0 and x % int(digit) == 0:
                    temp.append(digit)

            if len(temp) == len(st):
                res.append(x)

            temp = []
        return res
        