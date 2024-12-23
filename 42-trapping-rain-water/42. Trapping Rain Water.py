class Solution:
    def trap(self, height: List[int]) -> int:
        
        tallestR = [0] * len(height)
        tallestL = [0] * len(height)

        curr = float('-inf')
        for i in range(len(height)):
            curr = max(curr, height[i])
            tallestL[i] = curr

        curr = float('-inf')
        for i in range(len(height)-1, -1 , -1):
            curr = max(curr, height[i])
            tallestR[i] = curr
        
        ans = 0
        for i in range(len(height)):
            ans += min(tallestL[i], tallestR[i]) - height[i]

        return ans

        