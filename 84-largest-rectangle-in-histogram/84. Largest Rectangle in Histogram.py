class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] #idx, height
        ans = 0
        for i in range(n + 1):
            
            h = heights[i] if i < n else float("inf")
            start = i

            while stack and (i == n or stack[-1][1] > h):
                idx, height = stack.pop()
                start = idx
                width = i - idx
                ans = max(ans, width * height)
            
            if i < n:
                stack.append([start, heights[i]])
        
        

        
        
        return ans
