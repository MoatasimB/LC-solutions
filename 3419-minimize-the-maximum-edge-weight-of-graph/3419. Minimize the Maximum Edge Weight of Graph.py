class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        


        adj = defaultdict(list)
        mmax = 0
        for x, y, w in edges:
            mmax = max(mmax, w)
            adj[y].append((x, w))
        
        def check(mid):
            seen = set()
            seen.add(0)
            q = deque([0])

            while q:
                node = q.popleft()
                for nei, w in adj[node]:
                    if w > mid:
                        continue
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            return len(seen) == n
        
        
        l = 0
        r = mmax + 1
        removable = float('inf')
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                removable = min(mid, removable)
                r = mid - 1
            else:
                l = mid + 1

        if removable == float('inf'):
            return -1 
 
        
        return removable



        