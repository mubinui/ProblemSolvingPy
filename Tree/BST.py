class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, array):
        self.array = array
        self.idx = -1

    def node_builder(self):
        self.idx += 1
        if self.array[self.idx] == -1:
            return None

        data = self.array[self.idx]
        node = Node(data)
        node.left = self.node_builder()
        node.right = self.node_builder()
        return node

    def inorder_tree_traversal(self, root):
        if root is None:
            return
        self.inorder_tree_traversal(root.left)
        print(root.data, end=' ')
        self.inorder_tree_traversal(root.right)

    def preorder_tree_traversal(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder_tree_traversal(root.left)
        self.preorder_tree_traversal(root.right)

    def postorder_tree_traversal(self, root):
        if root is None:
            return

        self.postorder_tree_traversal(root.left)
        self.postorder_tree_traversal(root.right)
        print(root.data, end=' ')







