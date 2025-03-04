class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum = sum(nums[:k])
        max_avg = temp_sum / k 

        for i in range(k, len(nums)):
            temp_sum += nums[i] - nums[i - k] 
            max_avg = max(max_avg, temp_sum / k)

        return max_avg  