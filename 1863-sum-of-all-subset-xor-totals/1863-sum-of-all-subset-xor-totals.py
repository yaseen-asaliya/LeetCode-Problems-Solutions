class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        
        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return

            dfs(index + 1, current_xor ^ nums[index])

            dfs(index + 1, current_xor)
        
        dfs(0, 0)
        return self.total