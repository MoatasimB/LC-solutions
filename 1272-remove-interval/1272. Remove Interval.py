class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []

        startOfInterval, endOfInterval = toBeRemoved

        for start, end in intervals:

            if end < startOfInterval or start > endOfInterval:
                ans.append([start, end])
            else:

                if start < startOfInterval:
                    ans.append([start, startOfInterval])
                
                if end > endOfInterval:
                    ans.append([endOfInterval, end])
        
        return ans