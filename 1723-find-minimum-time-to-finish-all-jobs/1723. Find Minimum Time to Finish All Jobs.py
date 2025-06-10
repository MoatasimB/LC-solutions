class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        def check(mid):
            workers = [0] * k

            def dfs(i):

                if i == len(jobs):
                    return True
                
                for j in range(k):
                    if workers[j] + jobs[i] <= mid:
                        workers[j] += jobs[i]
                        if dfs(i + 1):
                            return True
                        workers[j] -= jobs[i]
                    if workers[j] == 0:
                        return False
                return False
            return dfs(0)

        l = max(jobs)
        r = sum(jobs)
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return l