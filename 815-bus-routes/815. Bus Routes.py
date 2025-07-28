class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        


        class Node:
            def __init__(self):
                self.children = set()
            
        if target == source:
            return 0
        nodes = []
        for route in routes:
            node = Node()
            for i in range(len(route)):
                node.children.add(route[i])
            nodes.append(node)

        graph = defaultdict(list)
        for i in range(len(nodes)):
            node1 = nodes[i]
            for j in range(i+1, len(nodes)):
                node2 = nodes[j]
                
                for children in node1.children:
                    if children in node2.children:
                        graph[node1].append(node2)
                        graph[node2].append(node1)
        
        q = deque()
        seen = set()
        
        for i in range(len(nodes)):
            if source in nodes[i].children:
                q.append((nodes[i], 0))
                seen.add(nodes[i])
                
        


        while q:

            curr, dist = q.popleft()

            if target in curr.children:
                return dist + 1
            
            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist + 1))
        
        return -1
            





