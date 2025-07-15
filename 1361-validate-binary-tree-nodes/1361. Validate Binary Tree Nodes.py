class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        

        inDeg = [0] * n
        g = defaultdict(list)
        for i in range(n):
            if leftChild[i] != -1:
                inDeg[leftChild[i]] += 1
                g[i].append(leftChild[i])
                g[leftChild[i]].append(i)

            if rightChild[i] != -1:
                inDeg[rightChild[i]] += 1
                g[i].append(rightChild[i])
                g[rightChild[i]].append(i)
        
        seen = set()
        def dfs(node):
            
            if node in seen:
                return
            
            seen.add(node)

            for nei in g[node]:
                dfs(nei)
        
        dfs(0)

            

        total_deg = 0
        for val in inDeg:
            if val > 1:
                return False
            total_deg += val
        
        return (total_deg) == n - 1 and len(seen) == n


        
