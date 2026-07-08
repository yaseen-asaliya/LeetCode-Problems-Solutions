class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        x = len(s) - 1

        while x >= 0:

            if s[x] == '#':
                res = chr(int(s[x-2] + s[x-1]) + 96) + res
                x-=2
            else:
                res = chr(int(s[x]) + 96) + res

            x-=1

        return res
