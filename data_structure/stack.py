class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def empty(self):
        return False if self.size() else True

    def top(self):
        if self.empty() is False:
            return self.stack[self.size() - 1]
        else:
            return False

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        return self.stack.pop()


if __name__ == "__main__":
    s = Stack()
    assert s.size() == 0
    assert s.empty() is True
    s.push("a")
    s.push("b")
    s.push("c")
    assert s.size() == 3
    assert s.empty() is False
    assert s.top() == "c"
    assert s.size() == 3
    assert s.pop() == "c"
    assert s.pop() == "b"
    assert s.pop() == "a"
    assert s.empty() is True
