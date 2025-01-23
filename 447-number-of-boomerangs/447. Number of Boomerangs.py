class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        ans = 0
        for i in range(len(points)):
            seen = defaultdict(int)
            for j in range(len(points)):
                center = points[i]

                curr = points[j]

                dist = (center[0] - curr[0])**2 + (center[1] - curr[1])**2

                if dist in seen:
                    ans += 2 * seen[dist]
                    seen[dist] +=1
                else: 
                    seen[dist] =1
        
        return ans