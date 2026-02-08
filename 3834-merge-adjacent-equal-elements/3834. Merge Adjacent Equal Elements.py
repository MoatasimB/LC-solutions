class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:


        s = []

        for n in nums:
            if s and n == s[-1]:
                s[-1] *= 2
                while len(s) > 1 and s[-1] == s[-2]:
                    s.pop()
                    s[-1] *= 2
            else:
                s.append(n)

        return s
                