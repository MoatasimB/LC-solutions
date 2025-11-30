class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        

        n = len(s)
        if s[n - 1] == "1":
            return False
        
        q = deque()
        seen = set()

        q.append(0)
        seen.add(0)
        farthest = 0
        while q:
            idx = q.popleft()

            if idx >= n - 1:
                return True
            
            for j in range(max(farthest,idx + minJump), min(n, idx + maxJump + 1)):
                if s[j] == "0" and j not in seen:
                    seen.add(j)
                    q.append(j)
            farthest = max(farthest, idx + maxJump)
        return False



        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n - 1:
                return True
            
            for j in range(i + minJump, min(n, i + maxJump + 1)):
                if s[j] == "0" and dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)
            
        # if s[n - 1] == "1":
        #     return False
        
        # goal = n - 1

        # for i in range(n - 2, -1, -1):
        #     if s[i] == "1":
        #         continue
            
        #     if i + minJump <= goal <= i + maxJump:
        #         goal = i
        
        # return goal == 0


        # 00111010
