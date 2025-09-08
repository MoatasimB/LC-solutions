class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        

        counts = defaultdict(int)
        l = 0
        ans = 0
        pairs = 0
        for r in range(len(nums)):
            pairs += counts[nums[r]]
            counts[nums[r]] += 1

            # if counts[nums[r]] > 1:
            #     if counts[nums[r]] - 1 > 1 :
            #         pairs -= math.comb(counts[nums[r]] - 1, 2)
            #         pairs += math.comb(counts[nums[r]], 2)
            #     else:
            #         pairs += 1
            
            while pairs >= k:
                ans += len(nums) - 1 - r + 1
                counts[nums[l]] -= 1
                pairs -= counts[nums[l]]
                # if counts[nums[l]] > 1:
                #     pairs -= math.comb(counts[nums[l]], 2)
                #     counts[nums[l]] -= 1
                #     if counts[nums[l]] > 1:
                #         pairs += math.comb(counts[nums[l]], 2)
                # else:
                #     counts[nums[l]] -= 1
                l += 1
            
        
        return ans

        # [3,1,4,3,2,2,4]


        # 3 = 1
        # 1 = 0
        # 4 = 2
        # 2 = 2

        # pairs = 2

        # 4
        # while pairs >= k