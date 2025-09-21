class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid: ])

            return merge(left, right)
        
        def merge(left, right):
            temp = []

            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
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
        
        return mergeSort(nums)
                
