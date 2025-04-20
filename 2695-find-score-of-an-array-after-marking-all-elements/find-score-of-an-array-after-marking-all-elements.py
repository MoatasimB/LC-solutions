class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        marked = set()

        nums = [[num, i] for i, num in enumerate(nums)]
        num_len = len(nums)
        heapify(nums)
        score = 0
        while len(marked) < num_len:
            while nums and nums[0][1] in marked:
                heapq.heappop(nums)
       
            num, idx = heapq.heappop(nums)

            marked.add(idx)
            if idx + 1 < num_len:
                marked.add(idx + 1)
            if idx - 1 >= 0:
                marked.add(idx - 1)
            
            score += num
        
        return score
