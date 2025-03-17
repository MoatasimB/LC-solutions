class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        d = arr[0] - 1
        # k -= d
        if k - d <= 0:
            return k
        k -= d
        for i in range(len(arr)-1):
            if arr[i + 1] - arr[i] > k:
                return arr[i] + k
            diff = arr[i+1] - arr[i]
            if diff > 1:
                k -= diff - 1
        
        return arr[-1] + k
