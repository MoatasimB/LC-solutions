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

        string = []

        def dfs(root):
            if not root:
                string.append("N#")
                return
            
            string.append(str(root.val) + "#")
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(string)
        return "".join(string)
    # 1 2 N N 3 4 N N 5 N N 
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split('#')
        i = 0
        def dfs():
            nonlocal i
            if data[i] == "N":
                return None
            node = TreeNode(data[i])
            i += 1
            node.left = dfs()

            i+= 1
            node.right = dfs()

            return node
        
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))