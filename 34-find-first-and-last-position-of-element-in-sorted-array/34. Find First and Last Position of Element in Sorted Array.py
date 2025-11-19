class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        def binSR(val): #rightmost position of target
            
            l = 0
            r = len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] <= val:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            return ans
        
        def binSL(val): #leftmost position of target
            
            l = 0
            r = len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] < val:
                    l = mid + 1                    
                else:
                    r = mid - 1
                    ans = mid
            
            return ans
        
        
        final = [binSL(target), binSR(target)]
        
        print(final)
        
        if nums[final[0]] != target or nums[final[1]] != target:
            return [-1,-1]
          
        
        return final
                    
                    