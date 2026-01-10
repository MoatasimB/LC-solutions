class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        mpp = defaultdict(int)
        MOD = 10**9 + 7
        for x, y in points:
            mpp[y] += 1
        
        total_edges = 0
        for y, edges in mpp.items():
            total_edges += ((edges * (edges - 1)) // 2) % MOD
        ans = 0
        print(total_edges)
        for y, edges in mpp.items():
            count = ((edges * (edges - 1)) // 2) % MOD
            other = total_edges - count
            ans += (count * other) % MOD
 
        return (ans // 2) % MOD