class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(mid):
            #mid is the largest sum we can have
            splits = 0

            curr = 0
            for num in nums:
                if num + curr > mid:
                    curr = 0
                    splits += 1
                
                curr += num
                # if curr > mid:
                #     return False
            
            return splits + 1 <= k


        l = max(nums)
        r = sum(nums)

        ans = float("inf")
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

