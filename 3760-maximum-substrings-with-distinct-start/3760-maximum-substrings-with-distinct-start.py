class Solution:
    def maxDistinct(self, s: str) -> int:
        n=set(s)
        return len(set(s))