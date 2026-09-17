class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        

        #subarray {} [i..j] : length
        # (i1, j1), (i2, j2)


        subarrays = []

        n = len(arr)
        l = 0
        curr = 0
        for i in range(n):
            curr += arr[i]

            while curr > target:
                curr -= arr[l]
                l += 1
            if curr == target:
                subarrays.append((l, i, i - l + 1))
        

        subarrays.sort(key=lambda x: x[0])
        m = len(subarrays)
        if m == 1:
            return -1
        l = 0
        r = m - 1

        ans = float("inf")
        print(subarrays)
        while l < r:
            s1, e1, l1 = subarrays[l]
            s2, e2, l2 = subarrays[r]

            if s2 <= e1:
                l += 1
                r -= 1
            else:
                ans = min(ans, l1 + l2)
                if l1 > l2:
                    l += 1
                else:
                    r -= 1
        
        l = 0
        r = m - 1
        while l < r:
            s1, e1, l1 = subarrays[l]
            s2, e2, l2 = subarrays[r]

            if s2 <= e1:
                l += 1
                r -= 1
            else:
                ans = min(ans, l1 + l2)
                if l1 >= l2:
                    l += 1
                else:
                    r -= 1
        
        return ans if ans != float("inf") else -1
