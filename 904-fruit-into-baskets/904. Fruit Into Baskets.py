class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        ans = 0
        l = 0
        mpp = defaultdict(int)

        for r in range(len(fruits)):
            mpp[fruits[r]] += 1

            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
