class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        i = 0

        while True:
            if i >= len(strs[0]):
                return res

            current = strs[0][i]

            for x in strs:
                if i >= len(x) or x[i] != current:
                    return res
            
            res += current
            i += 1