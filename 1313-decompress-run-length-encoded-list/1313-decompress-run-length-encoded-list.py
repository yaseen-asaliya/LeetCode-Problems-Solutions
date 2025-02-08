class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for freq in range(0, len(nums), 2):
            for c in range(nums[freq]):
                res.append(nums[freq+1])

        return res
