class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        

        # 
        #       #
        #   #   #
        #   #   #   #


        #mono_dec

        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            
            stack.append(i)

        return stack