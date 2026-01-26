class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        minDiff = float("inf")
        ans = []
        for i in range(n - 1):
            x = arr[i]
            y = arr[i + 1]

            if abs(y - x) < minDiff:
                minDiff = abs(y - x)
                ans = [[x, y]]
            elif abs(y - x) == minDiff:
                ans.append([x, y])
        
        return ans