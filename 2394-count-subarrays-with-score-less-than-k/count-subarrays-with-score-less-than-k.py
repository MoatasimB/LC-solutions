class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        # [2 1 4 3 5]

        # [2 3 7 10 15]
        # pre = [nums[0]]
        # for i in range(1, len(nums)):
        #     pre.append(pre[-1] + nums[i])

    
        l = 0
        curr_sum = 0
        ans = 0
        for r in range(len(nums)):
            curr_sum += nums[r] #7
            curr_score = (curr_sum * (r - l + 1)) # 7 * (3) = 21
            
            while curr_score >= k:
                curr_sum -= nums[l] # 7 - 2 = 5
                l += 1
                curr_score = (curr_sum * (r - l + 1)) # 5
            
            ans += r - l + 1 #3
        
        return ans






        # mpp = {}

        # curr = 0

        # for i in range(len(nums)):

        #     curr += nums[i]


        #     if curr