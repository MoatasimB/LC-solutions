class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def binS_l(l, r, num):
            ans = float("inf")
            while l <= r:
                mid = (l + r) // 2
                if num + nums[mid] < lower:
                    l = mid + 1
                else:
                    ans = min(ans, mid)
                    r = mid - 1
            
            return ans if ans != float('inf') else - 1

        def binS_h(l, r, num):
            ans = float("-inf")
            while l <= r:
                print('0')
                mid = (l + r) // 2

                if num + nums[mid] <= upper:
                    ans = max(ans, mid)
                    l = mid + 1
                else:
                    r = mid - 1
            
            return ans if ans != float('-inf') else - 1

        final = 0
        for i in range(len(nums)):
            num = nums[i]
            idx_lower = binS_l(i+1, len(nums) - 1, num)
            idx_upper = binS_h(i+1, len(nums) - 1, num)

            if idx_lower == -1 or idx_upper == -1:
                continue
            final += idx_upper - idx_lower + 1
        
        return final
            
