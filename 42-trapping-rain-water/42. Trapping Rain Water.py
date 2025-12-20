class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftSide = [0] * n
        rightSide = [0] * n

        leftSide[0] = height[0]
        rightSide[n - 1] = height[n - 1]
        
        for i in range(1, n):
            leftSide[i] = max(leftSide[i -1], height[i])
        
        for i in range(n - 2, -1, -1):
            rightSide[i] = max(rightSide[i + 1], height[i])
        
        ans = 0
        for i in range(n):
            h = min(leftSide[i], rightSide[i])

            ans += max(0, h - height[i])
        
        return ans