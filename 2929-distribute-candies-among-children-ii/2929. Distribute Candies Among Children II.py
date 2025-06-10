class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #stars and bars to get total
        # subtract when someone gets more than limit and this
        # is symmetrical

        total = ((n+2) * (n+1)) // 2
        if n < limit:
            return total
        # a b c = n
        # a + limit + 1 , b , c = n - limit - 1 
        x = n - limit + 1 
        extra_single = (x * ( x - 1) )// 2

        # a + limit + 1 , b + limit + 1 , c = n - 2 * limit - 2

        z = n - (2 * limit)
        if z < 1:
            return max(0,total - (3 * extra_single))

        extra_double = (z * ( z - 1) )// 2


        # a + limit + 1 , b + limit + 1 , c + limit + 1= n - 3 * limit - 3
        w = n - (3 * limit) - 1

        if w < 1:
            return max(0,total - (3 * extra_single) + (3 * extra_double))
        
        
        extra_triple = (w * (w - 1)) // 2
        return max(0,total - (3 * extra_single) + (3 * extra_double) - extra_triple)



        '''
        PIE 
        |A| when a gets more 
        |B| when b gets more
        |C| when c gets more

        - 

        |A n B|

        '''