class Solution(object):
    def sortColors(self, nums):
        ptr = 0
        target = 0

        for x in range(len(nums)):
            if nums[x] != target:
                ptr = x + 1

                while ptr < len(nums):
                    if nums[ptr] == target:
                        nums[x], nums[ptr] = nums[ptr], nums[x]
                        break
                    ptr += 1

            if nums[x] != target:
                target += 1
                if target > 2:
                    break

                if nums[x] != target:
                    ptr = x + 1
                    while ptr < len(nums):
                        if nums[ptr] == target:
                            nums[x], nums[ptr] = nums[ptr], nums[x]
                            break
                        ptr += 1