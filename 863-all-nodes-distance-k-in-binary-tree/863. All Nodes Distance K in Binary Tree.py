# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        ans = []

        q = deque()
        q.append((target, 0))
        seen = set()
        seen.add(target)

        while q:
            node, level = q.popleft()
            # print(node.val, level)
            if level == k:
                ans.append(node.val)
                continue
            if level > k:
                break
            seen.add(node)
            if node.left and node.left not in seen:
                q.append((node.left, level + 1))
            if node.right and node.right not in seen:
                q.append((node.right, level + 1))
            if node.parent and node.parent not in seen:
                q.append((node.parent, level + 1))
        
        return ans