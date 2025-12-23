class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        n = len(s)

        if s[n - 1] == "1":
            return False
        q = deque()
        seen = set()

        q.append([s[0], 0])
        seen.add(0)
        farthest = 0
        while q:    
            val, idx = q.popleft()

            if idx == n - 1:
                return True
            
            for j in range(max(farthest,idx + minJump), min(idx + maxJump + 1, n)):
                if j not in seen and s[j] == "0":
                    seen.add(j)
                    q.append([s[j], j])
            farthest = max(farthest, idx + maxJump + 1)
        
        return False