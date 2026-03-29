class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()

        for p in paths:
            start.add(p[0])
            end.add(p[1])
        
        for c in end:
            if c not in start:
                return c

