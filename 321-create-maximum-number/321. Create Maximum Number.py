class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:


        def getStack(i, arr):
            #we want from nums1 i best values
            #we want from nums2 k - i best values 
            stack = []
            m = len(arr)
            print(f"need to remove {m - i, m, i, arr}")
            #m - x = i
            # m - i values need to be removed 
            if (m - i) == 0:
                return arr
            removed = 0
            for idx, num in enumerate(arr):
                while stack and stack[-1] < num:
                    stack.pop()
                    removed += 1
                    if removed == m - i:
                        stack += arr[idx:]
                        break
                if removed == m - i:
                    break

                stack.append(num)
            while stack and len(stack) != i:
                stack.pop()
            return stack
        
        def check(a, b):
            ans = []
            i = j = 0

            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1

            return ans
        
        ans = []
        for i in range(max(0, k - len(nums2)), min(len(nums1) + 1, k + 1)):
            
            s1 = getStack(i, nums1)
            s2 = getStack(k - i, nums2)
            print(i, k - i, s1, s2)
            lst = check(s1, s2)
            ans = max(ans, lst)
        return ans
