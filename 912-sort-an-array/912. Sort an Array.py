class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, left, right):

            if left>=right:
                return
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)
        
        def merge(arr, left, mid, right):

            temp = []
            start1 = left
            start2 = mid + 1

            while start1 <= mid and start2 <= right:
                if arr[start1] < arr[start2]:
                    temp.append(arr[start1])
                    start1 +=1
                else:
                    temp.append(arr[start2])
                    start2 +=1


            while start1 <= mid:
                temp.append(arr[start1])
                start1+=1

            while start2 <= right:
                temp.append(arr[start2])
                start2+=1


            for i in range(left, right + 1):
                arr[i] = temp[i-left] 

        mergeSort(nums, 0, len(nums) - 1)

        return nums

