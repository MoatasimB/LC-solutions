class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        allPoints = defaultdict(int)

        for x, y in points:
            allPoints[(x,y)] += 1
        ans = float("inf")
        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue
                
                #point 3
                #point 4
                if (x1, y2) in allPoints and (x2, y1) in allPoints:
                    h = abs(y2 - y1)
                    w = abs(x2 - x1)
                    ans = min(ans, h * w)

        return ans if ans != float("inf") else 0

        # x1, y1.    !x2, y1



        # !x1,y2            x2, y2


        # !x1, y2           x2, y2



        # x1, y1            !x2, y1


                
