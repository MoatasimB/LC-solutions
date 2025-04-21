# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        r = []
        lefts = []
        leaves = []
        rights = []

        def leftB(node):
            if not node.left and not node.right:
                return
            lefts.append(node.val)
            if node.left:
                leftB(node.left)
            else:
                leftB(node.right)
        
        def rightB(node):
            if not node.left and not node.right:
                return
            rights.append(node.val)
            if node.right:
                rightB(node.right)
            else:
                rightB(node.left)

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if not node.left and not node.right:
                leaves.append(node.val)
    
        dfs(root)
        if root.left:
            leftB(root.left)
        if root.right:
            rightB(root.right)
        r.append(root.val)

        rights = rights[::-1]
        return r + lefts + leaves + rights

