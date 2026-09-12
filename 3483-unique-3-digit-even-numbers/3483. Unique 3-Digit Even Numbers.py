class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        n = len(digits)
        ans = set()
        def dfs(curr, seen):
            if curr >= 100:
                if curr % 2 == 0:
                    ans.add(curr)
                return
            
            for i in range(n):
                if curr == 0 and digits[i] == 0:
                    continue
                if i in seen:
                    continue
                seen.add(i)
                dfs((curr * 10)+ digits[i], seen)
                seen.remove(i)
        
        dfs(0, set())
        return len(ans)

        # dfs(0, 0)
        # dfs(1, 1)
        # dfs(12, 2)