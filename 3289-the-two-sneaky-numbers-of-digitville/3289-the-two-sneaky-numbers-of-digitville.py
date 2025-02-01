class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        res = []

        for index in range(len(nums) - 1):
            if nums[index] == nums[index+1]:
                res.append(nums[index])

        return res
