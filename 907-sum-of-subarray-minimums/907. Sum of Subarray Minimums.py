class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        stack = []
        answer  = 0
        n = len(arr)

        for right in range(n + 1):
            while stack and (right ==n or arr[stack[-1]] >= arr[right]):
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                numSubs = (mid - left) * (right - mid)

                answer += numSubs * arr[mid]

            stack.append(right)
        
        return answer % ((10**9) + 7)
