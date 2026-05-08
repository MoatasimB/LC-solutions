class Solution:
    def minJumps(self, nums: List[int]) -> int:
        

        [[], [], [2], [3], [2], [], [2, 3]]

        n = len(nums)
        N = max(nums) + 1
        factors = [[] for _ in range(N)]

        for i in range(2, N):
            if not factors[i]:
                for j in range(i, N, i):
                    factors[j].append(i)
        

        edges = defaultdict(list)
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)

        q = deque()
        seen = set()

        seen.add(n - 1)
        q.append([n - 1, 0])

        while q:
            idx, step = q.popleft()
            if idx == 0:
                return step
            
            if idx > 0 and idx - 1 not in seen:
                seen.add(idx - 1)
                q.append([idx - 1, step + 1])
            if idx + 1 < n and idx + 1 not in seen:
                seen.add(idx + 1)
                q.append([idx + 1, step + 1])

            for factor in factors[nums[idx]]:
                for new_idx in edges[factor]:
                    if new_idx not in seen:
                        seen.add(new_idx)
                        q.append([new_idx, step + 1])
                edges[factor] = []
        


            
