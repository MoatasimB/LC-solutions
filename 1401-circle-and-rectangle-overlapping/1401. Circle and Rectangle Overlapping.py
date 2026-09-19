class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        

        mx, my = x1, y1
        dirs = [(0, 1), (1,0), (-1,0), (0,-1)]
        def valid(x, y):
            return x1 <= x <= x2 and y1 <= y <= y2
        
        seen = set()
        seen.add((mx, my))
        curr_dist = math.sqrt((xCenter - mx)**2 + (yCenter - my)**2)
        curr_point = [mx, my]
        q = deque([[mx, my]])
        while q:
            mx, my = q.popleft()
            newX, newY = mx, my
            for dx, dy in dirs:

                nx, ny = mx + dx, my + dy
                if valid(nx, ny) and (nx, ny) not in seen:
                    distance = math.sqrt((xCenter - nx)**2 + (yCenter - ny)**2)
                    seen.add((nx, ny))
                    if distance < curr_dist:
                        
                        curr_dist = distance
                        curr_point = [nx, ny]
            if [newX, newY] != curr_point:
                q.append(curr_point)
            

        
        fx, fy = curr_point
        distance = math.sqrt((xCenter - fx)**2 + (yCenter - fy)**2)
        if distance <= float(radius):
            return True
        return False


        