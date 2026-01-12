# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = defaultdict(list)
        parents = {}
        deepest = 0
        def dfs(node, depth, parent):
            nonlocal deepest
            if not node:
                return
            deepest = max(deepest, depth)
            parents[node] = parent
            level[depth].append(node)
            dfs(node.left, depth + 1, node)
            dfs(node.right, depth + 1, node)
        
        dfs(root, 0, -1)

        nodes = level[deepest]
        final = set([node for node in nodes])

        while len(final) != 1:
            next_final = set()

            for node in final:
                next_final.add(parents[node])
            
            final = next_final
        
        for node in final:
            return node
        

            