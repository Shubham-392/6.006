from .node.binaryNode import BinaryNode

class BinaryTree:
    def __init__(self, nodeType = BinaryNode):
        self.root = None
        self.nodeType = nodeType
        self.size = 0

    def __len__(self): return self.size

    def __iter__(self):
        if self.root:
            for node in self.root.subtree_iter():
                yield node.item
