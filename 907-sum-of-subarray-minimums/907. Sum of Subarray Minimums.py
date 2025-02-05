class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        

        stack = []
        ans = 0
        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >=arr[i]):

                mid = stack.pop()

                right = i
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                num_of_subs = (mid - left) * (right - mid)
                total = num_of_subs * arr[mid]
                ans += total
        
            stack.append(i)
        
        return ans % ((10**9) + 7)