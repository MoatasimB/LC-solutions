class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        N = len(nums)
        MOD = 10**9 + 7
        total = 0

        # DP with Pascal's Triangle for nCr
        C = [[0] * (k + 1) for _ in range(N + 1)]
        C[0][0] = 1
        
        for n in range(1, N + 1):
            C[n][0] = 1
            for r in range(1, k + 1):
                C[n][r] = (C[n - 1][r - 1] + C[n - 1][r]) % MOD
        for i in range(len(nums)):
            #find #subsequence it is the min and it is the max

            #it is less than all numbers to the right
            #it is greater than all numbers from the left
            curr = nums[i]
            for j in range(1, k):
                #min
                remainingNums = n - i - 1
                # numIsMin = math.comb(remainingNums, j) % MOD
                numIsMin = C[remainingNums][j]
                # print(curr, remainingNums, numIsMin)

                #max
                prevNums = i
                # numIsMax = math.comb(prevNums, j) % MOD
                numIsMax = C[prevNums][j]

                # print(curr, prevNums, numIsMax)
                # print("--------")
                total += curr * (numIsMin + numIsMax) % MOD
        
        return (total + (sum(nums) * 2) % MOD) % MOD
