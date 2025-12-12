class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        

        [0, 1, 3, 4, 2, 1]
        #find peak idx

        n = mountainArr.length()

        l = 0 
        r = n - 1
        top = float("-inf")
        peakIdx = -1
        while l <= r:
            mid = (l + r) // 2
            prev = -1
            if mid - 1 >= 0:
                prev = mountainArr.get(mid - 1)
            val = mountainArr.get(mid)
            
            nxt = -1

            if mid + 1 < n:
                nxt = mountainArr.get(mid + 1)

            if prev < val > nxt:
                peakIdx = mid
                top = val
                break
            elif prev < val:
                l = mid + 1
            else:
                r = mid - 1
        print(top, peakIdx)
        if target == top:
            return peakIdx
        def bs(l, r):

            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1
        
        def bs2(l, r):

            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return -1
        
        leftHalf = bs(0, peakIdx)

        if leftHalf != -1: return leftHalf

        rightHalf = bs2(peakIdx + 1, n - 1)

        return rightHalf

