"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class WrapInt:
    def __init__(self, val):
        self.val = val
    def get_val(self):
        return self.val
    def inc_val(self):
        self.val += 1
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
	# 1 3 5 ?????? 6 ????? ???

    # [1, [3, [5], [6]],  [2], [4]]
        #1 # 3 # 2 # 4 ## 5 ## 6
        
        string = []
        def dfs(root, id, parent):
            if not root:
                return
            
            node_id = chr(id.get_val() + 48)
            node_val = chr(root.val + 48)
            node_par = chr(parent + 48) if parent else 'N'

            string.append(node_id)
            string.append(node_val)
            string.append(node_par)

            curr = id.get_val()
            for child in root.children:
                id.inc_val()
                dfs(child, id, curr)
        dfs(root, WrapInt(1), None)
        print(string)
        return "".join(string)
      

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        node_par = {}

        for i in range(0, len(data), 3):
            node_id = ord(data[i]) - 48
            node_val = ord(data[i+1]) - 48
            par_node = ord(data[i+2]) - 48
            node_par[node_id] = (par_node, Node(node_val, []))
        
        for i in range(3, len(data), 3):

            curr_node_id = ord(data[i]) - 48
            node = node_par[curr_node_id][1]

            par_node_id = ord(data[i + 2]) - 48
            par_node = node_par[par_node_id][1]

            par_node.children.append(node)
        
        return node_par[ord(data[0]) - 48][1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))