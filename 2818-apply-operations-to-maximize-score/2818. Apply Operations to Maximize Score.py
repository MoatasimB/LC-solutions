class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        prime_counts = defaultdict(int)

        for num in nums:
            og = num
            count = 0
            for i in range(2, int(sqrt(num) + 1)):
                if num % i == 0:
                    count += 1
                    while num % i == 0:
                        num = num // i
            
            if num > 1:
                count += 1
            prime_counts[og] = count
        
        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)

        stack = []

        for i in range(len(nums)):
            while stack and prime_counts[nums[stack[-1]]] < prime_counts[nums[i]]:
                right[stack.pop()] = i
            
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)
        max_heap = [[-val, idx] for idx, val in enumerate(nums)] #val,idx
        heapify(max_heap)
        ans = 1
        while k:
            n, idx = heappop(max_heap)
            n = -n
            subs = (idx - left[idx]) * (right[idx] - idx)
            subs = min(subs, k)
            ans = (ans * pow(n, subs, 10**9 + 7)) % (10**9 + 7)

            k -= subs
        
        return ans

