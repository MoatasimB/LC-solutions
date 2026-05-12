class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key = lambda x: -(x[1] - x[0]))
        n = len(tasks)

        l = max(tasks[i][1] for i in range(n))
        r = sum(tasks[i][0] + tasks[i][1] for i in range(n))

        def check(energy):
            orig = energy
            for a, m in tasks:
                if m > energy:
                    return False
                energy -= a
                if energy < 0:
                    return False
            return True

        ans = None
        while l <= r:
            mid = (l + r) // 2
            print(mid)

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

        # [[1,3],[2,4],[10,11],[10,12],[8,9]]

            # 32.   31.    29      19.    9
        

        # [10, 12], [10, 11], [8, 9], [2, 4], [1, 3]

        # 32         22         12     4      2