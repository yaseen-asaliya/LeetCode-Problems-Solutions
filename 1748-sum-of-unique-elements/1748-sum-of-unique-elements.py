class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = {}
        s = 0

        for x in nums:
            if x in res:
                res[x]+=1
            else:
                res[x] = 1

        for key, value in res.items():
            if value == 1:
                s+=key

        return s