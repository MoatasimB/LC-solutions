class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 29 -> 6 12 18 24
        rem = {}
        rem[0] = -1
        curr = 0

        for i in range(len(nums)):
            curr = (curr + nums[i]) % k

            if curr in rem:
                if rem[curr] < i - 1:
                    return True
            else:
                rem[curr] = i
        return False
