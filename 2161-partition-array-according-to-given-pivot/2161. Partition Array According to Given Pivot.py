class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        

        less = []
        equal = []
        more = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                more.append(num)
        
        final = []

        for num in less:
            final.append(num)
        for num in equal:
            final.append(num)
        for num in more:
            final.append(num)
        
        return final
