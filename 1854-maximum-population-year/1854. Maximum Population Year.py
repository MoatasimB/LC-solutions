class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mpp = defaultdict(int)

        for x, y in logs:
            mpp[x] += 1
            mpp[y] -= 1
        
        curr = 0
        mmax = float('-inf')
        ans = None
        for year in sorted(mpp.keys()):
            curr += mpp[year]

            if curr > mmax:
                mmax = curr
                ans = year
        
        return ans
