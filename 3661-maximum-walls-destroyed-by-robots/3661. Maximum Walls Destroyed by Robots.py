class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        
        # __ | __ x __ | __ | __ x __ x __ |
        n = len(robots)
        if n == 0 or len(walls) == 0:
            return 0
        bots = sorted([(robots[i], distance[i]) for i in range(n)], key=lambda x: x[0])

        robotRanges = {} #robot[i] : [left, right]
        walls.sort()
        for i in range(n):
            prevRobot = bots[i - 1][0] if i - 1 >= 0 else 0
            nextRobot = bots[i + 1][0] if i + 1 < n else float("inf")
            leftRange = max(prevRobot + 1, bots[i][0] - bots[i][1], 0)
            rightRange = min(nextRobot - 1, bots[i][0] + bots[i][1])
            robotRanges[i] = [leftRange, rightRange]

        

        memo = {}
        #walls are at indexes 0 3 5 6 9 10 15
        def findFirst(val):
            m = len(walls)
            l = 0
            r = m - 1
            ans = m
            while l <= r:
                mid = (l + r) // 2

                if walls[mid] >= val:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        def findLast(val):
            m = len(walls)
            l = 0
            r = m - 1
            ans = m
            while l <= r:
                mid = (l + r) // 2

                if walls[mid] > val:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
            

        # 2 5 7

        #Is there a robot between curr ---- max distance
        def dfs(i, prevDir):
            if i == n:
                return 0
            
            if (i, prevDir) in memo:
                return memo[(i, prevDir)]
            
            pos = bots[i][0]
            leftStart, rightEnd = robotRanges[i]
            ans = 0

            #shoot left
            leftIdx = findFirst(leftStart)
            endIdx = findLast(pos)
            leftWalls = endIdx - leftIdx
            if prevDir == "R":
                   #x __ | | | | | | _ x |  |
                    prev_pos = bots[i - 1][0]
                    _, prev_right_end = robotRanges[i - 1]
                    
                    rightIdx = findLast(prev_right_end)
                    if leftIdx <= rightIdx:

                        overlapWalls = (rightIdx-leftIdx)
                        leftWalls -= overlapWalls
            ans = max(ans, leftWalls + dfs(i + 1, "L"))



            #how many walls between pos <= x <= rightEnd
                
            startIdx = findFirst(pos)
            rightIdx = findLast(rightEnd)
            rightWalls = rightIdx - startIdx
                
            ans = max(ans, rightWalls + dfs(i + 1, "R"))
            memo[(i, prevDir)] = ans
            return ans
        
        return dfs(0, "")

