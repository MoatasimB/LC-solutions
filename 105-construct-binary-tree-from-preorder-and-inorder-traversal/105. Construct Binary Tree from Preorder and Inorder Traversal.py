# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mpp = {}

        for i,val in enumerate(inorder):
            mpp[val] = i
        
        curr = 0
        def dfs(left, right):
            nonlocal curr
            if left > right:
                return None
            val = preorder[curr]
            root = TreeNode(val)
            curr +=1

            root.left = dfs(left, mpp[val] - 1)
            root.right = dfs(mpp[val] + 1, right)

            return root
        
        return dfs(0,len(preorder)-1)


            

        

