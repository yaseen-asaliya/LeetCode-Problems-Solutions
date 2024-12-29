class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        
        seen = set()
        duplicate = -1
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]
            