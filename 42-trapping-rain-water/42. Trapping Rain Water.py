class Solution:
    def trap(self, height: List[int]) -> int:
        
        minLeft = [0]
        n = len(height)
        minRight = [0] * n
        [0,0,0,0,0,0,0]
        
        for i in range(1, n):
            h = height[i - 1]
            minLeft.append(max(minLeft[-1], h))
        
        for i in range(n - 2, -1, -1):
            h = height[i + 1]
            minRight[i] = (max(minRight[i+1], h))
        
        # minRight.reverse()
        ans = 0

        for i in range(n):
            ans += max(0,min(minLeft[i], minRight[i]) - height[i])
        
        return ans
        