class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(num1, num2):
            return str(num1) + str(num2) > str(num2) + str(num1)
        def merge(left, right):
            i = 0
            j = 0
            temp = []
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1
            
            while i < len(left):
                temp.append(left[i])
                i += 1
            while j < len(right):
                temp.append(right[j])
                j += 1
            
            return temp

        def mergesort(l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r) // 2
            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)
            return merge(left, right)
        final = mergesort(0, len(nums) - 1)
        final = "".join([str(num) for num in final])
        
        return final if final[0] != "0" else "0"
