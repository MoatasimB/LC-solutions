class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #find x in arr
        n = len(arr)
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        
        pos = r

        l = r
        r = r + 1

        # l = ans - 1
        # r = ans

        while k > 0:
            distL = abs(arr[l] - x) if l >= 0 else float("inf")
            distR = abs(arr[r] - x) if r < n else float("inf")
            if distL <= distR:
                k -= 1
                l -= 1
            else:
                k -= 1
                r += 1
        
        return arr[l+1 : r]
            