class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2
        
        max_area = 0
        
        for a, b, c in combinations(points, 3):
            max_area = max(max_area, area(a, b, c))
        
        return max_area