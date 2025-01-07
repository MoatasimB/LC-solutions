class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        def dfs(i, curr, target):
            if target == 0:
                ans.append(curr[:])
                return
            
            for j in range(i, len(candidates)):
                if target - candidates[j] < 0:
                    continue
                curr.append(candidates[j])
                target-= candidates[j]
                dfs(j, curr, target)
                
                curr.pop()
                target += candidates[j]
        
        dfs(0, [], target)
        return ans
            