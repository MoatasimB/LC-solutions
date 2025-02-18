class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            divisors = 0
            count = 0
            for j in range(1, int(math.sqrt(nums[i]) + 1)):
                if nums[i] % j == 0:
                    count += 1
                    if nums[i] // j != j:
                        count += 1
                    # if count > 4:
                    #     break
                    divisors += j
                    if nums[i] // j != j:
                        divisors += nums[i] // j
            if count == 4:
                ans += divisors

        
        return ans

                    

