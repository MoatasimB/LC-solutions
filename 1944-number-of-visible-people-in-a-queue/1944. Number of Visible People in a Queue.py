class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)

        stack = [] #mono dec

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] < h:

                ans[stack.pop()] += 1
            
            if stack:
                ans[stack[-1]] += 1
            
            stack.append(i)
        
        return ans
