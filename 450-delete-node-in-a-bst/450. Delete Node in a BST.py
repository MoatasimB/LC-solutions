# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #successor = go right -> go all the way left

        def dfs(root, key):
            if not root:
                return None
            
            if key < root.val:
                root.left = dfs(root.left, key)
            elif key > root.val:
                root.right = dfs(root.right, key)
            else:
                if not root.right:
                    return root.left
                if not root.left:
                    return root.right

                next = root.right

                while next.left:
                    next = next.left
                
                #switch these two nodes vals
                root.val = next.val

                #Now we need to delete that last node
                root.right = dfs(root.right, next.val)

            return root
        
        return dfs(root,key)