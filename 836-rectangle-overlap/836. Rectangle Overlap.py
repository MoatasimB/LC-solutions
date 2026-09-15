class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        

        x1, y1, x2, y2 = rec1

        r1, w1, r2, w2 = rec2

        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        
        return (intersect(x1, x2, r1, r2) and # width > 0
                intersect(y1, y2, w1, w2))    # height > 0

            # min(x2, r2) > max(x1, r1)

            #         x2, y2
            # x1, y1
        #check if rectangle above
            # top y1 cord is less than bottom y2 cord 

        #check if rectangle below:
            # bottom 1 cord is greater than top y2 cord
        return not ((y2 <= w1) or  (y1 >= w2) or (x2 <= r1) or (x1 >= r2))