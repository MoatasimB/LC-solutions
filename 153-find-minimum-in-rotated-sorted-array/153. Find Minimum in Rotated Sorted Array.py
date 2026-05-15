class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        l = 0
        r = n - 1
        ans = float("inf")
        while l <= r:
            mid = (l + r) // 2
            

            curr = nums[mid]
            ans = min(ans, curr, nums[l], nums[r])
            

            if nums[l] <= nums[mid]:
                if nums[l] <= nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
        
                r = mid - 1
        
        return ans

            