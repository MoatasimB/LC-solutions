class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        

        for i in range(len(nums)):

            j = i
            count = 1
            first = False
            while j < len(nums) - 1 and count < k:
                if nums[j] < nums[j + 1]:
                    count += 1
                    j += 1
                else:
                    break
            
            if count == k:
                first = True
            
            if first:
                j = i + k
                count = 1
                while j < len(nums) - 1 and count < k:
                    if nums[j] < nums[j + 1]:
                        count += 1
                        j += 1
                    else:
                        break
                
                if count == k:
                    return True
        
        return False


