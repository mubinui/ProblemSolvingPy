import Tree.BST as bst

array = [1, 2, 3, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
tree_01 = [1, 2, 4, -1, -1, 5, 8, -1, -1, 9, -1, -1, 3, 6, -1, 10, -1, -1, 7, -1, -1]

binary_search_tree = bst.BST(array)
root = binary_search_tree.node_builder()
# print(root.data)
# inorder tree traversal
binary_search_tree.inorder_tree_traversal(root)
print()
binary_search_tree.preorder_tree_traversal(root)
print()
binary_search_tree.postorder_tree_traversal(root)
print()
binary_search_tree.level_order_traversal(root)
print()
n = binary_search_tree.count_node(root)
print(n)
print('----------------------------------------------------->')
print("Tree Two")
binary_tree = bst.BST(tree_01)
tree_root = binary_tree.node_builder()
print('Number of nodes in the tree ', binary_tree.count_node(tree_root))
print('height of the tree is ',binary_tree.count_height(tree_root))

