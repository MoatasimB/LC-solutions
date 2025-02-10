class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        one = None
        two = None
        one_c = 0
        two_c = 0

        for i in range(len(nums)):
            if nums[i] == one:
                one_c += 1
            elif nums[i] == two:
                two_c += 1
            elif one_c == 0:
                one = nums[i]
                one_c = 1
            elif two_c == 0:
                two = nums[i]
                two_c = 1
            else:
                two_c -= 1
                one_c -= 1
        
        ans = []

        if one_c > 0 and nums.count(one) > len(nums) / 3:
            ans.append(one)
        if two_c > 0 and nums.count(two) > len(nums) / 3:
            ans.append(two)
        
        return ans