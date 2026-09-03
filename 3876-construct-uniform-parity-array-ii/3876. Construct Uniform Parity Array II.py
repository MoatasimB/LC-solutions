class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        
        #smallest even > largest odd
        se = float("inf")
        so = float("inf")
        odd_count = 0
        for num in nums1:
            if num % 2 == 0:
                se = min(se, num)
            else:
                so = min(so, num)
                odd_count += 1
        
        return se > so or odd_count == 0

        #odd - even = odd
        #odd - odd = odd
        # if len(nums1) 

        # for num in nums1:
        #     if num % 2 == 0:
        #         even_count += 1
        #     else:
        #         odd_count += 1
        
        # if odd_count == 0 or even_count == 0:
        #     return True
        
        # if odd_count >= 2 or even_count >= 2:
        #     return True
        
        # return False