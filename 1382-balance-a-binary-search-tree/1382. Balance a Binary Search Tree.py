# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        lst = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def create(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = TreeNode(lst[mid])
            node.left = create(l, mid - 1)
            node.right = create(mid + 1, r)

            return node
        
        return create(0, len(lst) - 1)