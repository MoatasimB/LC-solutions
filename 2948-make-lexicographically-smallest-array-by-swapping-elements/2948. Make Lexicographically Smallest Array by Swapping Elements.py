class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        groups = []

        # [1,7,6,18,2,1]
        # [1,1,2,6,7,18]

        # [0, 4, 5], [1, 2], [3]
        #  1.  2. 1.  7 6.    18
        # [0, 5, 4], [2, 1], [3]
        #  1. 1  2.   6  7.  18


        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort()
        n = len(nums)
        final = [0] * n
        
        curr = [new_nums[0][1]] #[val, idx]
        for i in range(1, n):
            if abs(new_nums[i][0] - new_nums[i - 1][0]) > limit:
                groups.extend(sorted(curr))
                curr = []
            curr.append(new_nums[i][1])
        
        
        if curr:
            groups.extend(sorted(curr))
        for i in range(n):
            idx = groups[i]
            val = new_nums[i][0]
            final[idx] = val
        return final
        

