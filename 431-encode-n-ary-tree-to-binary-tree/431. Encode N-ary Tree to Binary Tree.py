"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        rootNode = TreeNode(root.val)
        q = deque([[rootNode, root]])
        while q:
            binaryNode, node = q.popleft()
            prevNode = None
            headNode = None
            for children in node.children:
                newBNode = TreeNode(children.val)
                if prevNode:
                    prevNode.right = newBNode
                else:
                    headNode = newBNode
                prevNode = newBNode

                q.append([newBNode, children])
            binaryNode.left = headNode
        
        return rootNode
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        node = Node(data.val, [])

        #go to left child
            #keep going right
            #these are all of this Nodes children
        q = deque([[node, data]])
        while q:
            N_node, b_node = q.popleft()
            if b_node.left:
                curr = b_node.left
                new_n_node = Node(curr.val, [])
                N_node.children.append(new_n_node)
                q.append([new_n_node, curr])
                while curr.right:
                    curr = curr.right
                    new_n_node = Node(curr.val, [])
                    N_node.children.append(new_n_node)
                    q.append([new_n_node, curr])
        
        return node





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))