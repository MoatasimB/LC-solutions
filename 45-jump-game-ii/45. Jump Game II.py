class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()

        q.append([nums[0], 0, 0])
        seen = set()
        seen.add(0)

        farthest = 0
        while q:
            val, idx, steps = q.popleft()

            if idx == n - 1:
                return steps
            
            farthest = max(farthest, idx + 1)
            for j in range(farthest, min(idx + val + 1, n)):
                if j not in seen:
                    seen.add(j)
                    q.append([nums[j], j, steps + 1])
        


            
