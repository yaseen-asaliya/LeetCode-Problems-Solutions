class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        m = -1  

        for x in arr:
            dic[x] = dic.get(x, 0) + 1

        for key, val in dic.items():
            if key == val:
                m = max(m, key)

        return m