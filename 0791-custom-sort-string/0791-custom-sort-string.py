class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp = {}
        res = ""

        for c in s:
            temp[c] = temp.get(c, 0) + 1

        for o in order:
            if temp.get(o, 0) > 0:
                res += temp[o] * o
                temp[o] = 0

        for k ,v in temp.items():
            if v != 0:
                res += k * v

        return res 
        