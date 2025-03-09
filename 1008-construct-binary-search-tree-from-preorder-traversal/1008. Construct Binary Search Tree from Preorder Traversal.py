# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def create(mmin, mmax):
            nonlocal i
            if i == len(preorder):
                return None
            val = preorder[i]

            if val < mmin or val > mmax:
                return None
            i+=1
            node = TreeNode(val)

            node.left = create(mmin, val)
            node.right = create(val, mmax)

            return node
        
        return create(float('-inf'), float('inf'))
