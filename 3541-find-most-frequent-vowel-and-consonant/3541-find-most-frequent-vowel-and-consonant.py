class Solution:
    def maxFreqSum(self, s: str) -> int:
        gl = ['a', 'e', 'i', 'o', 'u']
        glas = {}
        sogl = {}
        for i in s:
            if i in gl:
                glas[i] = glas.get(i, 0) + 1
            else:
                sogl[i] = sogl.get(i, 0) + 1
        maxg = 0
        maxs = 0
        for _, value in glas.items():
            if value > maxg:
                maxg = value
        for _, v in sogl.items():
            if v > maxs:
                maxs = v
        return maxg+maxs
