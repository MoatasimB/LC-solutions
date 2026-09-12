class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        
        intervals = [interval + [idx] for idx, interval in enumerate(intervals)]
        intervals.sort()
        n = len(intervals)

        def find(i):
            start, end, _, _ = intervals[i]
            ans = n
            l = i + 1
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                s, _, _, _ = intervals[mid]
                if end < s:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        memo = {}
        def dfs(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if i >= n or k == 0:
                return (0, ())
            
            s, e, w, idx = intervals[i]
            skip_score, skip_indices = dfs(i + 1, k)
            next_idx = find(i)
            pick_score, pick_indices = dfs(next_idx, k - 1)
            pick_score += w
            pick_indices = tuple(sorted((idx,) + pick_indices))

            if skip_score > pick_score:
                memo[(i, k)] = (skip_score, skip_indices)
                return (skip_score, skip_indices)
            if pick_score > skip_score:
                memo[(i, k)] = (pick_score, pick_indices)
                return (pick_score, pick_indices)
            memo[(i, k)] = (pick_score, min(skip_indices, pick_indices))
            return (pick_score, min(skip_indices, pick_indices))
        
        return dfs(0, 4)[1]
