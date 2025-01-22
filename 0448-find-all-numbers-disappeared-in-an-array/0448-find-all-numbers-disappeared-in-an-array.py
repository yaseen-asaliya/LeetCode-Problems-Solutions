class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        nums = set(nums)
        res = []

        for num in range(1, l + 1):
            if not num in nums:
                res.append(num)

        return res

        