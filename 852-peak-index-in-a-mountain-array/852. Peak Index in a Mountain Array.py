class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 0
        r = len(arr) - 1

        while l<=r:
            mid = (l+r) // 2

            prior = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
            curr = arr[mid]
            after = arr[mid + 1] if mid + 1 < len(arr) else float('inf')

            if prior < curr  and after < curr:
                return mid
            elif prior < curr < after:
                l = mid + 1
            elif prior > curr >  after:
                r = mid - 1
        
        