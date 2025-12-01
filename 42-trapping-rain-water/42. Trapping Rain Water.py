class Solution:
    def trap(self, height: List[int]) -> int:


        n = len(height)


        leftMax = 0
        rightMax = 0

        l = 0
        r = n - 1
        ans = 0
        while l <= r:

            leftMax = max(leftMax, height[l])

            rightMax = max(rightMax, height[r])

            if leftMax < rightMax:
                ans += max(0, leftMax - height[l])
                l += 1
            else:
                ans += max(0, rightMax - height[r])
                r -= 1
        
        return ans






        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        
        right[-1] = height[-1]

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        

        ans = 0

        for i in range(n):
            threshold = min(left[i], right[i])

            ans += max(0, threshold - height[i])
        
        return ans