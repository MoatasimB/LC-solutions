class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] #idx, height
        ans = 0
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                start = idx
                width = i - idx
                ans = max(ans, width * height)
            
            stack.append([start, h])
        
        n = len(heights)

        while stack:
            idx, height = stack.pop()
            ans = max(ans, (n - idx) * height)
        
        return ans
