class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count+=1
        return count