class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        res = list(s)

        vals = []
        for c in s:
            if c in vowels:
                vals.append(c)

        vals.sort()

        idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                res[i] = vals[idx]
                idx += 1

        return "".join(res)