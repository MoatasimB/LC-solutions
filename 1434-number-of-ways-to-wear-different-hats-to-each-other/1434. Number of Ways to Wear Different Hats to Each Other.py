class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        

        hatsPerPerson = defaultdict(list)

        for i in range(len(hats)):
            for j in range(len(hats[i])):
                hatsPerPerson[hats[i][j]].append(i)
        

        mask = 0
        done = 2**len(hats) - 1
        MOD = 10**9 + 7
        memo = {}
        def dfs(hat, mask):
            if (hat, mask) in memo:
                return memo[(hat, mask)]
            if mask == done:
                return 1
            if hat > 40:
                return 0
            

            ans = 0
            ans += dfs(hat + 1, mask)

            for person in hatsPerPerson[hat]:
                if mask & (1 << person) == 0:
                    ans += dfs(hat + 1, mask | (1 << person)) % MOD
            memo[(hat, mask)] = ans % MOD
            return ans % MOD
        
        return dfs(1, 0)
        