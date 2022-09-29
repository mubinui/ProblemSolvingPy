import Tree.BST as bst

array = [1, 2, 3, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

binary_search_tree = bst.BST(array)
root = binary_search_tree.node_builder()
# print(root.data)
# inorder tree traversal
binary_search_tree.inorder_tree_traversal(root)
print()
binary_search_tree.preorder_tree_traversal(root)
print()
binary_search_tree.postorder_tree_traversal(root)
