class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n


        stack = [] #idx

        for i, height in enumerate(heights):

            while stack and heights[stack[-1]] <= height:
                ans[stack.pop()] += 1
            
            if stack:
                ans[stack[-1]] += 1
            
            stack.append(i)
        
        return ans