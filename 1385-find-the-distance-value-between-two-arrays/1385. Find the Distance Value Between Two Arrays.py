class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        n = len(arr1)
        m = len(arr2)

        # [4 5 8]. [1, 8, 9 10]
        # [1, 2, 3, 4, 5, 5, 5, 5, 7, 8, 9]
        def findPos(num):
            l = 0
            r = m - 1
            ans = m
            while l <= r:
                mid = (l + r) // 2

                if arr2[mid] >= num:
                    ans = mid
                    r = mid - 1 
                else:
                    l = mid + 1
            return ans
        ans = 0
        for i in range(n):
            idx = findPos(arr1[i])
            idx = idx if idx != m else idx - 1
            dist = abs(arr2[idx] - arr1[i])
            dist2 = abs(arr2[idx - 1] - arr1[i]) if idx - 1 >= 0 else float("inf")
            if dist > d and dist2 > d:
                ans += 1
        
        return ans