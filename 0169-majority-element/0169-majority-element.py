class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}

        for x in nums:
            temp[x] = temp.get(x, 0) + 1 

        size = len(nums)
        for key, val in temp.items():
            if val > size / 2:
                return key
