class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp = {}
        s = set()

        for x in arr:
            if x in temp:
                temp[x] += 1
            else:
                temp[x] = 1
        
        for k,v in temp.items():
            if v in s:
                return False
            s.add(v)
        
        return True