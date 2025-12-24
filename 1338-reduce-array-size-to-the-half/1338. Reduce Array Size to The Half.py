class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        n = len(arr)

        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1
        
        ans = 0
        count = 0
        for values in sorted(freq.values(), reverse = True):
            count += values
            ans += 1
            if count >= n // 2:
                break
        
        return ans



        