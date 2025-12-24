class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        inDeg = [0] * n
        graph = defaultdict(list)
        for i in range(n):
            if leftChild[i] != -1:
                inDeg[leftChild[i]] += 1
                graph[i].append(leftChild[i])
            if rightChild[i] != -1:
                inDeg[rightChild[i]] += 1
                graph[i].append(rightChild[i])
        
        #All indeg should be 1 except a single node with indeg 0

        countZ = 0
        countOne = 0
        for i in range(n):
            if inDeg[i] == 0:
                countZ += 1
                cand = i
            elif inDeg[i] == 1:
                countOne +=1
            else:
                return False
        if countZ > 1 or countOne != n - 1:
            return False
        seen = set()
        seen.add(cand)
        def dfs(node):

            for nei in graph[node]:
                if nei in seen:
                    return False
                seen.add(nei)
                if not dfs(nei):
                    return False
            return True
        
        return dfs(cand) and len(seen) == n