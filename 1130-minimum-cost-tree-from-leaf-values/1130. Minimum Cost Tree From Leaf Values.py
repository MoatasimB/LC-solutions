class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        


        #level 0 = 1 leaf node
        #level 1 = 2 leaf node 
        #level 2 = 4 leaf node
        #level k = 2^k nodes max
        n = len(arr)
        ans = 0
        while len(arr) > 1:
            min_idx = arr.index(min(arr))
            num = arr[min_idx]
            print(min_idx)
            left = arr[min_idx - 1] if min_idx - 1 >= 0 else float("inf")
            right = arr[min_idx + 1] if min_idx + 1 <len(arr) else float("inf")
            ans += num * min(left, right)
            arr.pop(min_idx)
        
        return ans

