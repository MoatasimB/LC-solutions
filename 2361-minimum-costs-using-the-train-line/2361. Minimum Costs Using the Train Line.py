class Node:
    def __init__(self, id):
        self.id = id
        self.isExpress = False
    def __lt__(self, other):
        return self.id < other.id

class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)
        graph = defaultdict(list)
        reg_nodes = {} #reg_nodes id : node
        exp_nodes = {} #exp_nodes id : node
        for i in range(n + 1):
            reg_node = Node(i)
            express_node = Node(i)
            express_node.isExpress = True
            reg_nodes[i] = reg_node
            exp_nodes[i] = express_node

        for i in range(n):
            reg_node = reg_nodes[i]
            express_node = exp_nodes[i]
            next_node = reg_nodes[i + 1]
            graph[reg_node].append([next_node, regular[i]])
            graph[reg_node].append([express_node, expressCost])
            graph[express_node].append([reg_node, 0])
            next_exp_node = exp_nodes[i + 1]
            graph[express_node].append([next_exp_node, express[i]])
        
        final_reg_node = reg_nodes[n]
        final_exp_node = exp_nodes[n]
        graph[final_reg_node].append([final_exp_node, expressCost])
        graph[final_exp_node].append([final_reg_node, 0])

        heap = [[0, reg_nodes[0]]] #cost, node
        reg_dists = [float("inf")] * (n + 1)
        reg_dists[0] = 0
        exp_dists = [float("inf")] * (n + 1)

        while heap:
            cost, node = heapq.heappop(heap)

            if node.isExpress:
                if cost > exp_dists[node.id]:
                    continue
            else:
                if cost > reg_dists[node.id]:
                    continue

            for nei, c in graph[node]:
                if nei.isExpress:
                    if c + cost < exp_dists[nei.id]:
                        exp_dists[nei.id] = c + cost
                        heapq.heappush(heap, [c + cost, nei])

                else:
                    if c + cost < reg_dists[nei.id]:
                        reg_dists[nei.id] = c + cost
                        heapq.heappush(heap, [c + cost, nei])
        final = [min(x, y) for x, y in zip(exp_dists, reg_dists)][1:]
        return final