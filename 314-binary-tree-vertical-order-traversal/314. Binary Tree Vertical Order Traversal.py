# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        leftMost = 0
        rightMost = 0
        rows = 0
        mpp = defaultdict(list) #row, col : nodes
        def dfs(node, row, col):
            nonlocal leftMost, rightMost, rows
            leftMost = min(leftMost, col)
            rightMost = max(rightMost, col)
            rows = max(rows, row)
            if not node:
                return
            mpp[(row, col)].append(node.val)

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)

        # for location, nodes in mpp.items():
        #     if len(nodes) > 1:
        #         nodes.sort()
        
        ans = []
        for col in range(leftMost, rightMost + 1):
            curr = []
            for row in range(0, rows + 1):
                if (row, col) in mpp:
                    for val in mpp[(row, col)]:
                        curr.append(val)
            if curr:
                ans.append(curr)
        
        return ans
