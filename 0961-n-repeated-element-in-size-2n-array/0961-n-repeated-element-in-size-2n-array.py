class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        n = len(nums) // 2
        for key, val in freq.items():
            if val == n:
                return key
            