class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        

        total = n1 + n2

        half = total // 2

        l = 0
        r = n1

        # [1 2 3 4 5]
        # [9 10 11 13]

        while l <= r:
            midA = (l + r) // 2
            midB = half - midA

            preA = nums1[midA - 1] if midA - 1 >= 0 else float("-inf")
            aftA = nums1[midA] if midA < n1 else float("inf")

            preB = nums2[midB - 1] if midB - 1 >= 0 else float("-inf")
            aftB = nums2[midB] if midB < n2 else float("inf")


            if preA <= aftB and preB <= aftA:
                #two halves are sorted
                if total % 2 == 0:
                    return (max(preA, preB) + min(aftA, aftB)) / 2
                else:
                    return min(aftA, aftB)
            elif preA > aftB:
                r = midA - 1
            else:
                l = midA + 1


