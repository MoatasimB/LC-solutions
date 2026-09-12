class Solution:
    def maxValue(self, intervals: List[List[int]], k: int) -> int:
        
        n = len(intervals)
        intervals.sort()
        def find(i):
            start, end, _ = intervals[i]
            l = i + 1
            r = n - 1
            ans = n
            while l <= r:
                mid = (l + r) // 2

                mS, mE, _ = intervals[mid]

                if mS > end:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

        memo = {}
        def dfs(i, count):
            if i >= n or count == 0:
                return 0
            if (i, count) in memo:
                return memo[(i, count)]
            
            score = 0
            #pick
            n_idx = find(i)
            l, r, w = intervals[i]
            # n_idx = i + 1
            # while n_idx < n and intervals[n_idx][0] <= r:
            #     n_idx += 1
            pick = w + dfs(n_idx, count - 1)

            #skip
            skip = dfs(i + 1, count)
            score = max(pick, skip)
            memo[(i, count)] = score
            return score
        
        return dfs(0, k)
