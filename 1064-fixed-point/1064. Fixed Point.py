class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        

    #     0  1 2 3 4 5 6 7  8  9
    #    -2 -1 1 2 4 6 7 10 11 20

    
        n = len(arr)
        l = 0
        r = n - 1
        ans = float("inf")
        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == mid:
                ans = min(ans, mid)
                r = mid - 1
            elif arr[mid] < mid:
                l = mid + 1
            else:
                r = mid - 1
        
        return ans if ans != float("inf") else -1
