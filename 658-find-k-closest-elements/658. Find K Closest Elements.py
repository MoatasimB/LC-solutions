class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = 0 
        r = len(arr) - 1

        while r - l + 1 > k:
            distL = abs(x - arr[l])
            distR = abs(x - arr[r])
            if distL <= distR:
                r -= 1
            else:
                l += 1

        return arr[l:r + 1]