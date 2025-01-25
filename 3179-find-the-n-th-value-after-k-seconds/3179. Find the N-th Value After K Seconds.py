class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        arr = [1] * n

        for i in range(k):
            for j in range(1, len(arr)):
                arr[j] = arr[j-1] + arr[j]
        
        return arr[-1] % (10**9 + 7)