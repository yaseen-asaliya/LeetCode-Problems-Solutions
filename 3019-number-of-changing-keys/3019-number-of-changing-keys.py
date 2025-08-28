class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        c = 0

        for x in range(1, len(s)):
            if s[x] != s[x-1]:
                c+=1
        return c 