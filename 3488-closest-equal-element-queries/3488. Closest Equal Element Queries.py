class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        n = len(nums)
        mpp = defaultdict(list) #int : [indices of int]

        #bs to find idex
        #look before and after and get minimum dist both ways

        for i in range(n):
            mpp[nums[i]].append(i)
        print(mpp)
        ans = []
        for q in queries:
            idx = q
            val = nums[idx]

            lst = mpp[val]
            if len(lst) == 1:
                ans.append(-1)
                continue

            l = 0
            r = len(lst) - 1
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
            m = len(lst)
            prev = lst[(location - 1)% m] 
            nxt = lst[(location + 1) % m]
            final = float("inf")
            if prev!= None:
                prevDist = min(abs(idx - prev), abs(n - (idx - prev)), abs(n - (prev - idx)))
                final = min(final, prevDist)
            if nxt != None:
                forDist = min(abs(nxt - idx), abs(n - (nxt - idx)), abs(n - (idx - nxt)))
                final = min(final, forDist)
            # print(q, prev, nxt, final)


            ans.append(final)
        
        return ans
