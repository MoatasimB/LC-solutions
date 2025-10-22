class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n - 1


        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: 
                if nums[l] <= target <= nums[mid]:                
                    if nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
            
            else:
                #sorted nums[mid] ... nums[n - 1]
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
            
        return -1
                

