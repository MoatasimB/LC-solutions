class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #mono increasing

        stack = [] #[i, height]
        ans = 0
        for i, height in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > height:
                formerIdx , h = stack.pop()
                width = (i - formerIdx)
                length = h
                ans = max(ans, width * length)
                idx = min(formerIdx, idx)
                # print(idx)
            # print(idx, i)
            stack.append((idx, height))
            # print(stack)
        n = len(heights)
        while stack:
            i, h = stack.pop()

            width = (n - i)
            length = h

            ans = max(ans, width * length)

        return ans

