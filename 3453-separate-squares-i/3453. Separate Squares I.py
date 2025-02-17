class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(mid):
            areaAbove = 0
            areaBelow = 0

            for x,y,l in squares:
                top = y + l
                if top <= mid:
                    areaBelow += l * l
                elif y >= mid:
                    areaAbove += l * l
                else:
                    topLength = top - mid
                    areaAbove += topLength * l

                    bottomLength = mid - y
                    areaBelow += bottomLength * l
            if areaAbove - areaBelow == 0:
                return 1
            if areaAbove > areaBelow:
                return 2
            return 3
        
        l = 0
        r = 2 * 10**9
        ans = float('inf')
        while r - l > 10**(-5):
            mid = (l+r) / 2.0
            x = check(mid)
            if x == 1:
                ans = min(ans, mid)
                r = mid
            elif x == 2:
                l = mid
            else:
                r = mid
        
        return (l + r) / 2
