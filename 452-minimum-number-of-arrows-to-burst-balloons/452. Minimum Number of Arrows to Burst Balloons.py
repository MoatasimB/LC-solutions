class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        curr = points[0][1]

        i = 1
        ans = 1
        while i < len(points):

            if points[i][1] < curr:
                i+=1
                continue
            elif points[i][0] > curr:
                ans +=1
                curr = points[i][1]
            i+=1

        return ans
