# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        

        ans = 0
        def dfs(node):
            nonlocal ans

            if not node:
                return [0,0]
            
            left,lc = dfs(node.left)
            right,rc = dfs(node.right)

            total = node.val + left + right

            cnt = 1 + lc + rc
            # if node.left:
            #     cnt += 1
            # if node.right:
            #     cnt += 1
            
            avg = total // cnt
            if avg == node.val:
                ans += 1

            return [total, cnt]
        
        dfs(root)

        return ans

                # 1
                #     3
                #         1
                #             3