class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res=0
        count=Counter(nums)

        for key,v in count.items():
            if(v%k==0):
                res+=key*v
                
        return res