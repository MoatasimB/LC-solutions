class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(arr, start, end):
            i = start
            j = end

            while i<=j:
                arr[i], arr[j] = arr[j], arr[i]
                i +=1
                j -=1
            return arr
        n = len(nums)
        nums = reverse(nums, 0, n-k-1)
        print(nums)
        nums = reverse(nums, n-k, n-1)
        print(nums)
        return reverse(nums, 0, n-1)