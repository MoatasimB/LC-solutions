class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:

        ans = -1
        smallestG = float("inf")


        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < smallestG:
                smallestG = capacity[i]
                ans = i

        return ans
                