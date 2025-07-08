class Solution:
    def hammingWeight(self, n: int) -> int:
        num_str = str(bin(n))
        count = 0

        for x in num_str:
            if x == '1':
                count+=1
        
        return count 
        
