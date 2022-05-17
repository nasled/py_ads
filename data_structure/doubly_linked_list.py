from singly_linked_list import SinglyLinkedList


class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        node = DoublyLinkedListNode(value)
        self.length = self.length + 1

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove(self, value):
        if self.head is None:
            return False
        if self.head.value is value:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length = self.length - 1
            return True
        node = self.head.next
        while node and node.value is not value:
            node = node.next
        if node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length = self.length - 1
            return True
        elif node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length = self.length - 1
            return True
        return False

    def reverse_traversal(self):
        node = self.tail
        while node:
            yield node.value
            node = node.prev


if __name__ == "__main__":
    dll = DoublyLinkedList()
    assert dll.length == 0
    dll.add("a")
    dll.add("b")
    dll.add("c")
    assert "c" == dll.head.value
    assert "b" == dll.head.next.value
    assert "b" == dll.head.next.next.prev.value
    assert dll.length == 3
    dll.add("d")
    dll.add("e")
    dll.add("f")
    assert "f" == dll.head.value
    assert "e" == dll.head.next.value
    assert "e" == dll.head.next.next.prev.value
    assert dll.length == 6
    assert list(dll.traverse()) == ["f", "e", "d", "c", "b", "a"]
    assert list(dll.reverse_traversal()) == ["a", "b", "c", "d", "e", "f"]
    assert dll.remove("j") is False
    assert dll.remove("a") is True
    assert dll.remove("f") is True
    assert dll.contains("e") is True
    assert dll.contains("a") is False
    assert list(dll.traverse()) == ["e", "d", "c", "b"]
    assert list(dll.reverse_traversal()) == ["b", "c", "d", "e"]
    assert dll.length == 4
    assert dll.head.value == "e"
    assert dll.tail.value == "b"
