class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_lst = list(str(num))

        last_seen = [-1] * 10

        for i in range(len(nums_lst)):
            last_seen[int(nums_lst[i])] = i
        
        for i in range(len(nums_lst)):
            for d in range(9, int(nums_lst[i]), -1):
                if last_seen[d] > i:
                    nums_lst[i], nums_lst[last_seen[d]] = nums_lst[last_seen[d]], nums_lst[i]
                    return int("".join(nums_lst))

        return num