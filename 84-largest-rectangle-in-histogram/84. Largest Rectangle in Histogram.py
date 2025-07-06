class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)
        for i in range(len(heights)):
            start = i
            while stack and heights[stack[-1][0]] > heights[i]:
                idx, left = stack.pop()
                start = min(start, left)
                ans = max(ans, (i - left) * heights[idx])
            
            stack.append((i, start))

        
        while stack:
            idx, left = stack.pop()
            ans = max(ans, (n - left) * heights[idx])
        
        return ans


