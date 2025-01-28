class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        for e1 in arr1:
            valid = True
            for e2 in arr2:
                if abs(e1 - e2) <= d:
                    valid = False
                    break
            if valid:
                c += 1
        return c
        