# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(root, key):
            if not root:
                return None
            
            if root.val < key:
                root.right = dfs(root.right, key)
            elif root.val > key:
                root.left = dfs(root.left, key)
            
            else:

                if not root.left and not root.right:
                    return None
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    f = root.right
                    while f.left:
                        f = f.left
                    
                    root.val = f.val
                    root.right = dfs(root.right, f.val)
            return root
        return dfs(root, key)