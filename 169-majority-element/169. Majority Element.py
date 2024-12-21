class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        el = None

        for num in nums:
            if count == 0:
                el = num
                count +=1
            else:
                if num == el:
                    count+=1
                else:
                    count -= 1
        return el

            