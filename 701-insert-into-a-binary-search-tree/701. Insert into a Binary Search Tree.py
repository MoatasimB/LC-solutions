# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def dfs(root):
            if not root:
                return TreeNode(val)
            
            # if not root.left and val < root.val:
            #     root.left = TreeNode(val)
            #     return root
            # elif not root.right and val > root.val:
            #     root.right = TreeNode(val)
            #     return root


            if val < root.val:
                root.left = dfs(root.left)
            else:
                root.right = dfs(root.right)

            # if left == None:
            #     if val < root.val:
            #         root.left = TreeNode(val)
            # if right == None:
            #     if val > root.val:
            #         root.right = TreeNode(val)
            
            return root
        
        return dfs(root)
