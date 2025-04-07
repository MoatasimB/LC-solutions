class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        mmax = float('-inf')
        ans = None
        for i in range(len(logs)):
            curr = 0
            x, y = logs[i]
            for j in range(len(logs)):
                s, e = logs[j]

                if s <= x < e:
                    curr += 1

            if curr > mmax:
                mmax = curr
                ans = x

        return ans
        
        
        
        
        
        
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
