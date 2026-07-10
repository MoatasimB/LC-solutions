

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        components = [0] * n
        curr = 0
        for i in range(1, n):
            prevNum = nums[i - 1]
            currNum = nums[i]

            if abs(prevNum - currNum) > maxDiff:
                curr += 1
            components[i] = curr
        return [(components[x] == components[y]) for x, y in queries]
       