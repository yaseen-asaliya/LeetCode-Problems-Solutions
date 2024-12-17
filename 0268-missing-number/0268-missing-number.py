class Solution(object):
    def missingNumber(self, nums):
        # use summation formula 
        length = len(nums)
        expected_sum = length * (length + 1) // 2  
        actual_sum = sum(nums)          
        return expected_sum - actual_sum