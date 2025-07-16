"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class Wint:
    def __init__(self, val):
        self.val = val
    def inc(self):
        self.val +=1
    def get_val(self):
        return self.val

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        string = []

        def dfs(root, id, parent):

            if not root:
                return
            
            node_val = chr(root.val + 48)
            node_id = id.get_val()
            node_par = chr(parent + 48) if parent else 'N'

            string.append(chr(node_id + 48))
            string.append(node_val)
            string.append(node_par)

            for child in root.children:
                id.inc()
                dfs(child, id, node_id)

        dfs(root, Wint(1), None)
        return "".join(string)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        parent_node_dic = {}

        for i in range(0, len(data), 3):

            node_id = ord(data[i]) - 48
            node_val = ord(data[i+1]) - 48
            node_par = ord(data[i+2]) - 48

            parent_node_dic[node_id] = [node_par, Node(node_val, [])]
        
        for i in range(3, len(data), 3):
            node_id = ord(data[i]) - 48
            node_val = ord(data[i+1]) - 48
            node_par = ord(data[i+2]) - 48
            
            child = parent_node_dic[node_id][1]
            parent = parent_node_dic[node_par][1]
            parent.children.append(child)
        
        return parent_node_dic[ord(data[0]) - 48][1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))