class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        holding = defaultdict(int)
        ans = 0
        for r in range(len(fruits)):
            holding[fruits[r]] += 1
            while len(holding) > 2:
                holding[fruits[l]] -= 1
                if holding[fruits[l]] == 0:
                    del holding[fruits[l]]
                l+=1
            
            ans = max(ans, r - l + 1)
            print(r, l)
        
        return ans
