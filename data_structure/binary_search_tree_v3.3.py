from standard_queue import StandardQueue
from binary_search_tree import BinarySearchTreeNode, BinarySearchTree


class BinarySearchTree33(BinarySearchTree):
    """
    yield from is available in pep 380, therefore python 3.3 is required
    """
    def preorder(self, root_node):
        if root_node:
            yield root_node.value
            yield from self.preorder(root_node.left)
            yield from self.preorder(root_node.right)

    def postorder(self, root_node):
        if root_node:
            yield from self.postorder(root_node.left)
            yield from self.postorder(root_node.right)
            yield root_node.value

    def inorder(self, root_node):
        if root_node:
            yield from self.postorder(root_node.left)
            yield root_node.value
            yield from self.postorder(root_node.right)


if __name__ == "__main__":
    bst = BinarySearchTree33()
    bst.insert_value(23)
    bst.insert_value(14)
    bst.insert_value(31)
    bst.insert_value(7)
    bst.insert_value(17)
    bst.insert_value(9)
    assert bst.contains_value(7) is True
    assert bst.contains_value(0) is False
    assert bst.find_parent_value(7).value == 14
    assert bst.find_value(7).value == 7
    assert bst.length == 6
    bst.remove_value(7)
    assert bst.length == 5
    assert bst.contains_value(7) is False
    assert bst.find_min_value().value == 9
    assert bst.find_max_value().value == 31
    assert list(bst.preorder(bst.root)) == [23, 14, 9, 17, 31]
    assert list(bst.postorder(bst.root)) == [9, 17, 14, 31, 23]
    assert list(bst.inorder(bst.root)) == [9, 17, 14, 23, 31]

    bst2 = BinarySearchTree33()
    for i in range(1, 10):
        bst2.insert_value(i)
    bst2.remove_value(4)
    assert list(bst2.preorder(bst2.root)) == [1, 2, 3, 5, 6, 7, 8, 9]
    assert list(bst2.postorder(bst2.root)) == [9, 8, 7, 6, 5, 3, 2, 1]
    assert list(bst2.inorder(bst2.root)) == [1, 9, 8, 7, 6, 5, 3, 2]
