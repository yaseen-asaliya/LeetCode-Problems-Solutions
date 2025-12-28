class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num, temp = 0, 0

        for num in nums:
            if num == 1:
                temp +=1 
            else:
                max_num = max(max_num, temp)
                temp = 0
                
        max_num = max(max_num, temp)

        return max_num
