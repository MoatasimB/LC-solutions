class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        m = len(classroom)
        n = len(classroom[0])
        def valid(r, c):
            return 0<=r < m and 0 <= c < n
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]
        start = None
        power = 0
        litter_spots = {} #(r, c) = power of two

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start = [r, c]
                elif classroom[r][c] == "L":
                    litter_spots[(r, c)] = power
                    power += 1

        q = deque()
        best = defaultdict(lambda: float("-inf"))
        final = 2**power -1
        q.append([start[0], start[1],energy,0, 0]) #r, c, energy, dist
        best[(start[0], start[1], 0)] = energy
        
        while q:
            r, c, curr_energy, curr_dist, mask = q.popleft()
            if mask == final:
                return curr_dist
            
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if valid(nr, nc) and classroom[nr][nc] != "X":
                    if curr_energy == 0:
                        continue
                    new_dist = curr_dist + 1
                    new_energy = curr_energy - 1
                    new_mask = mask
                    if classroom[nr][nc] == "R":
                        new_energy = energy
                    elif classroom[nr][nc] == "L":
                        power = litter_spots[(nr, nc)]
                        new_mask = mask | (1 << power)
                    
                    
                    
                    
                    # print(best[(nr, nc, new_mask)], nr, nc, new_mask, new_energy)
                    if best[(nr, nc, new_mask)] < new_energy:
                        best[(nr, nc, new_mask)] = new_energy
                        q.append([nr, nc, new_energy, new_dist, new_mask])

                            
        
        return -1

        [   "S.", 
            "XL"]
          
        # [
        #     "L.S", 
        
        #     "RXL"
        # ]
        # ["LS", 
        # "RL"]

        # [0, 1, 4, 0, 0]

        # (0, 0, 3, 1, 1)
        #     ()

        # (0, 0, 3, 1, 2)