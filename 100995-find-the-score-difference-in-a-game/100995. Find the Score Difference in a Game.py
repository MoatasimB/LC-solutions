class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player1= 0
        player2 = 0
        active = True
        swapIdx = 5

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                active = not active
            if i == swapIdx:
                active = not active
            if active:
                player1 += nums[i]
            else:
                player1 -= nums[i]
            if i == swapIdx:
                swapIdx += 6

        return player1
            
            