class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        

        mpp = {
            1 : [3, 7, 9], 
            2 : [8], 
            3 : [1, 7, 9],
            4 : [6],
            5 : [],
            6 : [4],
            7 : [1, 3, 9],
            8 : [2],
            9 : [1, 3, 7]
        }


        def dfs(node, count, seen):
            ans = 0
            if count > n:
                return 0
            if m <= count <= n:
                ans += 1
            
            for neighbor in [1,2,3,4,5,6,7,8,9]:
                if node == neighbor or neighbor in seen:
                    continue
                if neighbor not in mpp[node]:
                    seen.add(neighbor)
                    ans += dfs(neighbor, count + 1, seen)
                    seen.remove(neighbor)
                else:
                    requiredNode = (node + neighbor) // 2
                    if requiredNode in seen:
                        seen.add(neighbor)
                        ans += dfs(neighbor, count + 1, seen)
                        seen.remove(neighbor)

            return ans
        
        final = (4 * dfs(1, 1, set([1]))) + (4 * dfs(2, 1, set([2]))) + dfs(5, 1, set([5]))
        return final