class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = nums1[:]

        i = 0
        j = 0
        curr = 0
        while i < m and j < n:
            if x[i] < nums2[j]:
                nums1[curr] = x[i]
                i += 1
                curr +=1
            else:
                nums1[curr] = nums2[j]
                j +=1
                curr +=1
        while i < m:
            nums1[curr] = x[i]
            curr += 1
            i+=1

        while j < n:
            print(curr,j)
            nums1[curr] = nums2[j]
            curr += 1
            j+=1

