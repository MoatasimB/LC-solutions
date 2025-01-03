# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        self.inorder = [-1]
        self.dfs(self.root)
        self.pos = 0

    def next(self) -> int:
        self.pos +=1
        return self.inorder[self.pos]
        

    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.inorder)
    
    def dfs(self, root):

        if not root:
            return
        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)


        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()