# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []

        def dfs(node):
            if not node:
                data.append("N#")
                return
            data.append(str(node.val) + "#")
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return "".join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split("#")
        i = 0
        # [1, 2, N, N, 3, 4, N , N, 5, N, N]
        def dfs():
            nonlocal i
            if lst[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(lst[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))