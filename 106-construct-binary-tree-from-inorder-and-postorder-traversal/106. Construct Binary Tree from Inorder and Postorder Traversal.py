# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        mpp = {}

        for i,val in enumerate(inorder):
            mpp[val] = i

        def dfs(left, right):

            if left>right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            root.right = dfs(mpp[val] + 1, right)
            root.left = dfs(left, mpp[val]-1)
            return root
        
        return dfs(0,len(postorder)-1)
        