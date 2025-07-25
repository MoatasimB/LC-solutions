# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
                self.parent = None


        parents = {} #node, parent
        startNode = None
        def dfs(node, parent):
            nonlocal startNode
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

            if node.val == start:
                startNode = node
        

        dfs(root, TreeNode(-1))

        seen = set()

        q = deque()
        q.append([startNode, 0])
        ans = float("-inf")
        while q:
            node, time = q.popleft()

            if node in seen:
                continue
            
            ans = max(ans, time)
            seen.add(node)

            if node.left:
                q.append([node.left, time + 1])
            if node.right:
                q.append([node.right, time + 1])

            if node.parent and node.parent.val > 0:
                q.append([node.parent, time + 1])
        
        return ans

        


