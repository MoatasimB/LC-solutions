class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counts = defaultdict(int)
        n = len(nums)

        for num in nums:
            counts[num] += 1
        pairs = n // 2

        curr = 0

        for key,val in counts.items():
            curr += val // 2
        
        return pairs == curr