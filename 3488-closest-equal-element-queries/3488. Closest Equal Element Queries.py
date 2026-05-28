class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)

        count = defaultdict(int)
        closest = [float("inf")] * n
        prev = {}
        first = {}
        for i in range(n):
            count[nums[i]] += 1
            if nums[i] in prev:
                closest[i] = i - prev[nums[i]]
            if nums[i] not in first:
                first[nums[i]] = i
            prev[nums[i]] = i
        
        #handle edge case
        for num, firstIdx in first.items():
            if count[num] == 1:
                continue
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
            if count[num] == 1:
                continue
            firstIdx = first[num]
            if firstIdx == lastIdx:
                continue
            # print(num, firstIdx, lastIdx)
            dist = n - lastIdx + firstIdx
            closest[lastIdx] = min(closest[lastIdx], dist)
        
        print(closest)
        ans = []

        for q in queries:
            num = nums[q]
            if count[num] == 1:
                ans.append(-1)
            else:
                ans.append(closest[q])
        
        return ans
