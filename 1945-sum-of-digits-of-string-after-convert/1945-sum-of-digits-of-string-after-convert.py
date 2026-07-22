class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        
        for x in s:
            temp += str(ord(x) - 96)
            
        for a in range(k):
            ttl = 0
            for x in temp:
                ttl += int(x)
            temp = str(ttl)
        
        return int(temp)
