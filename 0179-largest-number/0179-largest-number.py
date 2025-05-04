class Solution:
    def bubble_sort(self, strings):
        n = len(strings)
        for i in range(n):
            for j in range(0, n - i - 1):
                if strings[j] + strings[j + 1] < strings[j + 1] + strings[j]:
                    strings[j], strings[j + 1] = strings[j + 1], strings[j]
        return strings
                    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums = self.bubble_sort(nums)

        result = ''.join(nums)
        return '0' if result[0] == '0' else result