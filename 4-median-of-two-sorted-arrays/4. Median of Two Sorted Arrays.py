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

        while l <= r:
            midA = (l + r) // 2
            midB = half - midA

            leftA = nums1[midA - 1] if midA - 1 >= 0 else float("-inf")
            rightA = nums1[midA] if midA < n1 else float("inf")
            
            leftB = nums2[midB - 1] if midB - 1 >= 0 else float("-inf")
            rightB = nums2[midB] if midB < n2 else float("inf")


            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1
            