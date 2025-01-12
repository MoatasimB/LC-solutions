class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        ans = 0
        # print(count)

        for k,v in count.items():
            if v > 1:
                ans += int((v * (v-1)) / 2)
        return ans