class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        #mono dec
        n = len(arr)
        MOD = 10**9 + 7
        stack = []

        ans = 0
        for i in range(n):

            while stack and arr[stack[-1]] >= arr[i]:
                #up to this idx top of stack is min

                idx = stack.pop()
                val = arr[idx]

                #right choices
                right = i - idx

                #left choices
                left = idx + 1
                if stack:
                    left = idx - stack[-1]
                

                numOfSubarrays = right * left
                ans += (val * numOfSubarrays) % MOD
            
            stack.append(i)
        
        # [3 1 2 4]

        # [1, 2, 4]
        # [1, 2, 3]

        while stack:
            idx = stack.pop()
            val = arr[idx]
            right = n - idx

                #left choices
            left = idx + 1
            if stack:
                left = idx - stack[-1]
            numOfSubarrays = right * left
            ans += (val * numOfSubarrays) % MOD
        
        return ans % MOD
