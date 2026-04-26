class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        ans = set()
        n = len(nums)
        for i in range(n):
            flag = True
            for j in range(i):
                if nums[i] <= nums[j]:
                    flag = False
                    break
            if flag:
                ans.add(i)

        for i in range(n - 1, -1, -1):
            flag = True
            for j in range(n - 1, i, -1):
                if nums[i] <= nums[j]:
                    flag = False
                    break
            if flag:
                ans.add(i)

        final = []
        for i in range(n):
            if i in ans:
                final.append(nums[i])

        return final
        ans = set()
        ans.add(0)
        n = len(nums)

        i = 1
        while i < n:
            if nums[i] > nums[i - 1]:
                ans.add(i)
                i += 1
            else:
                break

        if n == 1:
            return [nums[0]]

        ans.add(n - 1)
        i = n - 2
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                ans.add(i)
                i -= 1
            else:
                break

        final = []

        for i in range(n):
            if i in ans:
                final.append(nums[i])

        return final

        