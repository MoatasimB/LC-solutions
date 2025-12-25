class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftSide = 0
        rightSide = 0

        l = 0
        r = n - 1
        ans = 0
        while l < r:
            leftSide = max(leftSide, height[l])
            rightSide = max(rightSide, height[r])

            if leftSide < rightSide:
                ans += max(0, leftSide - height[l])
                l += 1
            else:
                ans += max(0, rightSide - height[r])
                r -= 1
            
        
        
        
        return ans