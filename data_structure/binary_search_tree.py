from standard_queue import StandardQueue
from stack import Stack


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert_value(self, value):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
            self.length = 1
        else:
            self.insert_node(self.root, value)
            self.length = self.length + 1

    def insert_node(self, current_node, value):
        if current_node.value > value:
            if current_node.left is None:
                current_node.left = BinarySearchTreeNode(value)
            else:
                self.insert_node(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = BinarySearchTreeNode(value)
            else:
                self.insert_node(current_node.right, value)

    def contains_value(self, value):
        return self.contains_node(self.root, value)

    def contains_node(self, root_node, value):
        if root_node is None:
            return False
        if root_node.value is value:
            return True
        elif root_node.value > value:
            return self.contains_node(root_node.left, value)
        else:
            return self.contains_node(root_node.right, value)

    def find_parent_value(self, value):
        return self.find_parent_node(self.root, value)

    def find_parent_node(self, root_node, value):
        if root_node.value is value:
            return None
        if root_node.value > value:
            if root_node.left is None:
                return None
            elif root_node.left.value is value:
                return root_node
            else:
                return self.find_parent_node(root_node.left, value)
        else:
            if root_node.right is None:
                return None
            elif root_node.right.value is value:
                return root_node
            else:
                return self.find_parent_node(root_node.right, value)

    def find_value(self, value):
        return self.find_node(self.root, value)

    def find_node(self, root_node, value):
        if root_node is None:
            return None
        if root_node.value is value:
            return root_node
        elif root_node.value > value:
            return self.find_node(root_node.left, value)
        else:
            return self.find_node(root_node.right, value)

    def find_min_value(self):
        return self.find_min_node(self.root)

    def find_min_node(self, root_node):
        if root_node.left is None:
            return root_node
        return self.find_min_node(root_node.left)

    def find_max_value(self):
        return self.find_max_node(self.root)

    def find_max_node(self, root_node):
        if root_node.right is None:
            return root_node
        return self.find_max_node(root_node.right)

    def depth_first_traverse(self):
        result = []
        root_node = self.root
        stack = Stack()
        while stack.empty() is False or root_node:
            if root_node:
                stack.push(root_node)
                root_node = root_node.left
            else:
                root_node = stack.pop()
                result.append(root_node.value)
                root_node = root_node.right
        return result

    def breadth_first_traverse(self):
        result = []
        root_node = self.root
        queue = StandardQueue()
        while root_node:
            result.append(root_node.value)
            if root_node.left:
                queue.enqueue(root_node.left)
            if root_node.right:
                queue.enqueue(root_node.right)
            if len(queue):
                root_node = queue.dequeue()
            else:
                root_node = None
        return result

    def zig_zag_traverse(self):
        result = []
        left_to_right_direction = True
        direction_queue = StandardQueue()
        active_queue = StandardQueue()
        active_queue.enqueue(self.root)
        while len(active_queue):
            node = active_queue.dequeue()
            result.append(node.value)
            if left_to_right_direction:
                if node.left:
                    direction_queue.enqueue(node.left)
                if node.right:
                    direction_queue.enqueue(node.right)
            else:
                if node.right:
                    direction_queue.enqueue(node.right)
                if node.left:
                    direction_queue.enqueue(node.left)
            if len(active_queue) == 0:
                left_to_right_direction = not left_to_right_direction
                active_queue = direction_queue
                direction_queue = StandardQueue()
        return result

    def remove_value(self, value):
        target_node = self.find_value(value)
        if target_node is None:
            return False
        if self.length == 1:
            self.root = None
        else:
            tree = BinarySearchTree()
            seq = self.breadth_first_traverse()
            for item in seq:
                if item != value:
                    tree.insert_value(item)
            self.root = tree.root
            self.length = tree.length
            return True


if __name__ == "__main__":
    bst = BinarySearchTree()
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
    assert bst.depth_first_traverse() == [9, 14, 17, 23, 31]
    assert bst.breadth_first_traverse() == [23, 14, 31, 9, 17]
    assert bst.zig_zag_traverse() == [23, 14, 31, 17, 9]

    bst2 = BinarySearchTree()
    bst2.insert_value(17)
    bst2.insert_value(14)
    bst2.insert_value(31)
    bst2.insert_value(9)
    bst2.remove_value(bst2.root.value)
    assert bst2.breadth_first_traverse() == [14, 9, 31]
