class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # nums.sort()
        # ans = 0

        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     if nums[i] + nums[j] == k:
        #         ans += 1
        #         i += 1
        #         j -= 1
        #     elif nums[i] + nums[j] > k:
        #         j -= 1
        #     else:
        #         i += 1
        # return ans
        # seen = [False] * len(nums)
        # dic = {}
        # ans = 0
        # for i in range(len(nums)):

        #     if (k - nums[i]) in dic:
        #         other = dic[k-nums[i]]
        #         if not seen[other] and not seen[i]:
        #             seen[other] = True
        #             seen[i] = True
        #             ans += 1
        #     dic[nums[i]] = i
        
        # return ans

        used = set()
        ans = 0
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        

        for key, val in counts.items():

            if (k - key) in counts and (k - key) not in used:
                print(key, k-key)
                if key == k - key:
                    ans += (val) // 2
                    used.add(key)
                    continue
                ans += min(val, counts[k-key])
                used.add(key)
                used.add(k-key)
        
        return ans