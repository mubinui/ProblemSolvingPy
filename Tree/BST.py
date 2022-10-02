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

    def level_order_traversal(self, root: Node):
        queue = [root, None]
        while len(queue) > 0:
            current_node = queue.pop(0)  # always pops the item from 0 index
            if current_node is None:
                print()
                # for printing the level
                if len(queue) > 0:
                    queue.append(None)
                else:
                    break
            else:
                print(current_node.data, end=' ')
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)

    def count_node(self, root):
        if root is None:
            return 0
        left_nodes = self.count_node(root.left)
        right_nodes = self.count_node(root.right)
        return left_nodes + right_nodes + 1  # adding 1 for every root

    def count_height(self, root):
        if root is None:
            return 0
        left_height = self.count_height(root.left)
        right_height = self.count_height(root.right)
        return max(left_height, right_height) + 1  # +1 is for the root

    # The diameter should be 6
    # def count_diameter(self, root):
    #     if root is None:
    #         return 0
    #
    #     left_side = self.count_diameter(root.left)
    #     right_side =self.count_diameter(root.right)
