class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        new = sorted([[num, i] for i, num in enumerate(arr)])
        if not arr:
            return [] 
        rank = 1
        n = len(arr)
        ans = [0] * n
        ans[new[0][1]] = rank
        for i in range(1, n):
            curr, idx = new[i]
            prev, p_idx = new[i - 1]

            if curr != prev:
                rank += 1
            
            ans[idx] = rank
        
        return ans