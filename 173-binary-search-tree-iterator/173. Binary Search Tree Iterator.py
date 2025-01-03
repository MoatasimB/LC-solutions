# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        self.inorder = []
        self.getLeft(self.root)

    def next(self) -> int:

        smallestNode = self.inorder.pop()
        smallestVal = smallestNode.val

        if smallestNode.right:
            self.getLeft(smallestNode.right)
        return smallestVal
        

    def hasNext(self) -> bool:
        return len(self.inorder) > 0
    def getLeft(self, root):

        if not root:
            return
        
        while root:
            self.inorder.append(root)
            root = root.left

        


        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()