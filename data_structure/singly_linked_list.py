class SinglyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        node = SinglyLinkedListNode(value)
        self.length = self.length + 1

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def contains(self, value):
        node = self.head
        while node:
            if node.value is value:
                return True
            node = node.next
        return False

    def remove(self, value):
        if self.head is None:
            return False
        node = self.head
        if node.value is value:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length = self.length - 1
            return True
        while node.next and node.next.value is not value:
            node = node.next
        if node.next is not None:
            if node.next is self.tail:
                self.tail = node
            else:
                node.next = node.next.next
            self.length = self.length - 1
            return True
        return False

    def traverse(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def reverse_traversal(self):
        if self.tail:
            current_node = self.tail
            while current_node is not self.head:
                previous_node = self.head
                while previous_node.next is not current_node:
                    previous_node = previous_node.next
                yield current_node.value
                current_node = previous_node
            yield current_node.value


if __name__ == "__main__":
    sll = SinglyLinkedList()
    assert sll.length == 0
    sll.add("a")
    sll.add("b")
    sll.add("c")
    assert sll.tail.value == "a"
    assert sll.head.value == "c"
    assert list(sll.traverse()) == ["c", "b", "a"]
    assert sll.length == 3
    assert sll.remove("c") is True
    sll.add("e")
    assert sll.length == 3
    assert list(sll.traverse()) == ["e", "b", "a"]
    assert sll.contains("e") is True
    assert sll.contains("c") is False
    assert list(sll.reverse_traversal()) == ["a", "b", "e"]
    assert sll.tail.value == "a"
    assert sll.head.value == "e"
    assert sll.remove("f") is False
    assert sll.remove("e") is True
    assert sll.remove("b") is True
    assert sll.remove("a") is True
    assert sll.length == 0
