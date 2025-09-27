from itertools import combinations

class Solution:
    def largestTriangleArea(self, points):
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

        max_area = 0.0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, area(p1, p2, p3))

        return max_area

points1 = [[0,0],[0,1],[1,0],[0,2],[2,0]]
points2 = [[1,0],[0,0],[0,1]]

print(Solution().largestTriangleArea(points1))
print(Solution().largestTriangleArea(points2))
