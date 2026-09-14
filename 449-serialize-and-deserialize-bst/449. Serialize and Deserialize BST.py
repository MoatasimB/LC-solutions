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
        if not root:
            return ""

        def dfs(root):
            if not root:
                ans.append("N")
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(str(root.val))

        
        dfs(root)
        return "#".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split("#")
        print(data)
        def dfs():
            if not data[-1]:
                return None
            if data and data[-1] == "N":
                data.pop()
                return None

            node = TreeNode(int(data.pop()))
            node.right = dfs()
            node.left = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# .........2
# .....1......3

# N N 1 N N 3 2

