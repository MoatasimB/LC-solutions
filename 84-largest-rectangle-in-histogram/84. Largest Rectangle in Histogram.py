class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(i, h)

        ans = 0
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][1] >= heights[i]:

                prevIdx, h = stack.pop()
                ans = max(ans, h * (i - prevIdx))
                idx = min(idx, prevIdx)
            
            stack.append([idx, heights[i]])
        

        while stack:
            idx, h = stack.pop()

            ans = max(ans, h * (len(heights) - idx))
        
        return ans

