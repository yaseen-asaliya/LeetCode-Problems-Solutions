class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_sum = 0
        even_sum = 0
        flag = True

        for x in num:
            if flag:
                even_sum += int(x)
                flag = False
            else:
                odd_sum += int(x)
                flag = True

        return even_sum == odd_sum