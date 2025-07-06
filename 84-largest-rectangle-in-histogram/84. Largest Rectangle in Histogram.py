class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] #[i, h]
        ans = float('-inf')
        for i, h in enumerate(heights):
            prev_idx = i
            while stack and h <= stack[-1][1]:
                idx, height = stack.pop()

                length = height
                width = i - idx
                ans = max(ans, length * width)
                prev_idx = idx
            
            stack.append([prev_idx, h])
        
        n = len(heights)
        for i in range(len(stack)):
            idx, h = stack[i]
            length = h
            width = n - idx
            ans = max(ans, length*width)
        
        return ans
