class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        

        def getTopSort(edges):

            indeg = [0] * (k + 1)
            graph = defaultdict(list)

            for a, b in edges:
                graph[a].append(b)
                indeg[b] += 1
            
            q = deque()

            for i in range(1, len(indeg)):
                if indeg[i] == 0:
                    q.append(i)
            ans = []
            while q:
                node = q.popleft()
                ans.append(node)

                for nei in graph[node]:
                    indeg[nei] -=1
                    if indeg[nei] == 0:
                        q.append(nei)
            
            return ans if len(ans) == k else -1
        
        rowTopSort = getTopSort(rowConditions)
        colTopSort = getTopSort(colConditions)

        if rowTopSort == -1 or colTopSort == -1:
            return []

        colMpp = {} #place this digit at colIdx : i

        for i in range(len(colTopSort)):
            colMpp[colTopSort[i]] = i
        
        # row = [[3,0], 1, 2]
        # col = [[3,0], 2, 1]


        # matrix = [
        #     3[0 0 0],
        #     1[0 0 0],
        #     2[0 0 0],
        #       3  2 1
        # ]

        matrix = [[0] * k for _ in range(k)]

        for i in range(len(rowTopSort)):
            digit = rowTopSort[i]
            row = i
            col = colMpp[digit]
            matrix[row][col] = digit
        
        return matrix
