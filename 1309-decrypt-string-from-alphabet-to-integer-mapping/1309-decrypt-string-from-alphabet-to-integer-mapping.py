class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        x = len(s) - 1

        while x >= 0:
            t = ""

            if s[x] == '#':
                t = s[x-2] + s[x-1]
                x-=2
            else:
                t = s[x]

            res = chr(int(t) + 96) + res
            x-=1

        return res
