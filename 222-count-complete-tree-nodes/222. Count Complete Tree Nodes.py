# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        x = root
        height = 0

        while x.left:
            height +=1
            x = x.left
        leafNodes = 0
        if height == 0:
            return 1
        stack = []
        stack.append([root,0])

        while stack:
            node,level = stack.pop()

            if level == height -1 and (not node.left or not node.right):
                if node.left or node.right:
                    leafNodes +=1
                break
            
            if level == height - 1:
                if node.left:
                    leafNodes +=1
                if node.right:
                    leafNodes +=1
            else:
                if node.right:
                    stack.append((node.right, level + 1))
                if node.left:
                    stack.append((node.left, level + 1))
        
        ans = 0
        for i in range(height):
            ans += 2**i
        
        ans += leafNodes
        return ans



        