class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def mergeSort(l, r):
            if l >= r:
                return

            mid = (l + r) // 2
            
            mergeSort(l, mid)
            mergeSort(mid + 1, r)

            merge(l, mid, r)
        
        def merge(left, mid, right):
            temp = []

            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            
            for i in range(left, right + 1):
                nums[i] = temp[i - left]
        
        mergeSort(0, len(nums) - 1)

        return nums
                
