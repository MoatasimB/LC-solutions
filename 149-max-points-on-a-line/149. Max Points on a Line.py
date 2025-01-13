class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ans = 1
        for i in range(len(points)):
            dic = defaultdict(int)
            for j in range(i + 1, len(points)):
                curr = 1
                pointA = points[i]
                pointB = points[j]
                if pointA[0] != pointB[0]:
                    slope = (pointA[1] - pointB[1]) / (pointA[0] - pointB[0])
                else:
                    slope = float('inf')
                if slope not in dic:
                    curr += 1
                    dic[slope] = 2
                else:
                    dic[slope] += 1
                    curr = dic[slope]
                
                ans = max(ans, curr)
        
        return ans
