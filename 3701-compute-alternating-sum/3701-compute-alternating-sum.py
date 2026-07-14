class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        flag = True
        s = 0

        for x in nums:
            if flag:
                s += x
                flag = False
            else:
                s -= x
                flag = True
        
        return s