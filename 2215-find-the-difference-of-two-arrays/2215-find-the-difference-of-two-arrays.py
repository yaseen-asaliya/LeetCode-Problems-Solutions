class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = [[], []]

        for n in nums1:
            if n in nums1 and not n in nums2:
                res[0].append(n)
        
        for n in nums2:
            if n in nums2 and not n in nums1:
                res[1].append(n)

        return res