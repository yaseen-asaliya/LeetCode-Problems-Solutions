class Solution:
    def maximum69Number(self, num: int) -> int:
        num = list(str(num))

        for index in range(len(num)):
            if num[index] == '6':
                num[index] = '9'
                break

        return int(''.join(num))