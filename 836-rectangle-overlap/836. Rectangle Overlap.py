class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        

        x1, y1, x2, y2 = rec1

        r1, w1, r2, w2 = rec2

        #check if rectangle above
            # top y1 cord is less than bottom y2 cord 

        #check if rectangle below:
            # bottom 1 cord is greater than top y2 cord
        return not ((y2 <= w1) or  (y1 >= w2) or (x2 <= r1) or (x1 >= r2))