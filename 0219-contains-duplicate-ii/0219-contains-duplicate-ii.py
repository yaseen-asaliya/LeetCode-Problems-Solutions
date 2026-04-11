class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        p1, p2 = 0, 0
        myset = set() 

        for p2 in range(len(nums)):
            if nums[p2] in myset:
                return True
            
            myset.add(nums[p2])
            if abs(p1-p2) >= k:
                myset.remove(nums[p1])
                p1+=1

        return False
