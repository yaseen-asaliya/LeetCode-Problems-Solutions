class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        num_of_0s = 0
        num_of_1s = 0

        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                nums[index] = 0
                num_of_0s +=1
            else:
                nums[index] = 1
                num_of_1s += 1

        
        return [0] * num_of_0s + [1] * num_of_1s
