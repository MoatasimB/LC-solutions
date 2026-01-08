class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        

        # 1,1,2,2,3,4,4,8,8

        # 0 1 2 3 4 5 6 7 8


        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            val = nums[mid]
            prev = nums[mid - 1] if mid - 1 >= 0 else None
            next = nums[mid + 1] if mid + 1 < len(nums) else None

            if prev and val == prev:
                if mid % 2 == 1:
                    l = mid + 1
                else:
                    r = mid - 1
            elif next and val == next:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return nums[mid]