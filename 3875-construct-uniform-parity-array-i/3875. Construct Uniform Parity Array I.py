class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        # even - even = even
        # even - odd = odd
        # odd - odd = even
        # odd - even = odd

        #already all even
        #or two odds

        odd_count = 0
        even_count = 0

        for num in nums1:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        if odd_count == 0 or even_count == 0:
            return True
        
        if odd_count >= 1 or even_count >= 1:
            return True
        
        return False