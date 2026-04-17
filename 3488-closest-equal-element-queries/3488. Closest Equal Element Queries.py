class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        n = len(nums)
        mpp = defaultdict(list) #int : [indices of int]

        #bs to find idex
        #look before and after and get minimum dist both ways

        for i in range(n):
            mpp[nums[i]].append(i)
        
        
        ans = []
        for q in queries:
            idx = q
            val = nums[idx]

            lst = mpp[val]
            m = len(lst)
            if m == 1:
                ans.append(-1)
                continue

            l = 0
            r = m - 1
            location = None
            while l <= r:
                mid = (l + r) // 2
                if lst[mid] == idx:
                    location = mid
                    break
                elif lst[mid] < idx:
                    l = mid + 1
                else:
                    r = mid - 1
            
            prevIdx = lst[(location - 1) % m] 
            nextIdx = lst[(location + 1) % m]
            
            prevDist = min(abs(idx - prevIdx), abs(n - (idx - prevIdx)), abs(n - (prevIdx - idx)))
            forDist = min(abs(nextIdx - idx), abs(n - (nextIdx - idx)), abs(n - (idx - nextIdx)))


            ans.append(min(prevDist, forDist))
        
        return ans
