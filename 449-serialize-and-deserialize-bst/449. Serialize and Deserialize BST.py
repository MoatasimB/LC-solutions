# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []

        def dfs(root):
            if not root:
                ans.append("N#")
                return
            ans.append(str(root.val) + "#")
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return "".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        i = 0
        data = data.split("#")
        print(data)
        def dfs():
            nonlocal i
            if data[i] == "N":
                return None

            node = TreeNode(data[i])
            i += 1
            node.left = dfs()
            i += 1
            node.right = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans