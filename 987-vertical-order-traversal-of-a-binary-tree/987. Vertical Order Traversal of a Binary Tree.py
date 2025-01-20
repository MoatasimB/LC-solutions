# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        cols = defaultdict(list)

        def dfs(root,row, col):
            if not root:
                return
            
            cols[col].append((row, root.val))

            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
        
        dfs(root,0, 0)
        ans = []


        mmin = min(cols.keys())
        mmax = max(cols.keys())

        for i in range(mmin, mmax + 1):
            if i in cols:
                lst = cols[i]
                # print(lst)
                lst.sort()
                ans.append([el[1] for el in lst])
        # for key, val in sorted(cols.items()):
        #     val.sort()
        #     ans.append(val)
        print(ans)
        return ans
