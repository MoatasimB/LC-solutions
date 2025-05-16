class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        

        #mono_dec

        stack = []
        ans = [0] * len(heights)

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] <= h:

                idx = stack.pop()
                ans[idx] += 1
            
            if stack:
                ans[stack[-1]] += 1

            stack.append(i)
        
        return ans