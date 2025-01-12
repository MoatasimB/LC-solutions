class Solution:
    def mySqrt(self, x: int) -> int:
        
        # if x == 0:
        #     return 0
        # if x == 1 or x == 2:
        #     return 1
        for i in range(x+1):
            if i*i >= x:
                if i*i == x:
                    return i
                return i-1
        return 0
