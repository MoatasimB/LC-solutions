class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        goal = total // 4

        matchsticks.sort(reverse = True)

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]
            
            for j in range(i, len(matchsticks)):
                for k in range(4):
                    if sides[k] + matchsticks[j] > goal:
                        continue
                    sides[k] += matchsticks[j]
                    if dfs(j + 1):
                        return True
                    sides[k] -= matchsticks[j]            

                return False
            return False
        return dfs(0)