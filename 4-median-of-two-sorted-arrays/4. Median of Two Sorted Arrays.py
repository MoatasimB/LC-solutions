class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        [1,2,3,4,5]
        [1,2,3,4,5,6,7,8,9,10]
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        A = len(nums1)
        B = len(nums2)

        total = A+B
        half = (total // 2)
        l = 0
        r = A - 1
        while True:

            mid = (l + r) // 2
            second = half - mid - 2
            
            pointA = nums1[mid] if mid >= 0 else float('-inf')
            rightA = nums1[mid+1] if mid + 1 < A  else float('inf')
            
            pointB = nums2[second] if second >= 0 else float('-inf')
            rightB = nums2[second + 1] if second + 1 < B else float('inf')

            if rightA >= pointB and rightB >= pointA:

                if total % 2 != 0:
                    return min(rightA, rightB)
                
                return (max(pointA, pointB) + min(rightA, rightB)) / 2
            
            elif pointA > rightB:
                r = mid - 1
            else:
                l = mid + 1

                
            