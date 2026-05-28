class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)

        closest = [float("inf")] * n
        prev = {}
        first = {}
        for i in range(n):
            if nums[i] in prev:
                closest[i] = i - prev[nums[i]]
            if nums[i] not in first:
                first[nums[i]] = i
            prev[nums[i]] = i
        
        #handle edge case
        for num, firstIdx in first.items():
            backwards = prev[num]
            if backwards == firstIdx:
                continue
            dist = firstIdx + (n - backwards)
            closest[firstIdx] = dist
        print(closest)
        #do from right
        next = {}
        for i in range(n - 1, -1, -1):
            if nums[i] in next:
                closest[i] = min(closest[i], next[nums[i]] - i)
            next[nums[i]] = i
            

        print(closest)
        #handle edge case
        for num, lastIdx in prev.items():
            firstIdx = first[num]
            if firstIdx == lastIdx:
                continue
            # print(num, firstIdx, lastIdx)
            dist = n - lastIdx + firstIdx
            closest[lastIdx] = min(closest[lastIdx], dist)
        
        print(closest)
        ans = []

        for q in queries:
            
            ans.append(closest[q] if closest[q] != float("inf") else -1)
        
        return ans
