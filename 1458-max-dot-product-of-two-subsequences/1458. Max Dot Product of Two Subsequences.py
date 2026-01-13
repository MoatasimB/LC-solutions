class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(nums1) and j == len(nums2):
                return 0
            if i == len(nums1) or j == len(nums2):
                return float("-inf")


            ans = max((nums1[i] * nums2[j]) + max(0, dfs(i + 1, j + 1)), dfs(i + 1, j), dfs(i, j + 1))
            
            memo[(i, j)] = ans

            return ans
        
        return dfs(0, 0)