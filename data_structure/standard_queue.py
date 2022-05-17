class StandardQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue):
            return self.queue[0]
        else:
            return None


if __name__ == "__main__":
    sq = StandardQueue()
    sq.enqueue('a')
    sq.enqueue('b')
    sq.enqueue('c')
    sq.enqueue('d')
    sq.enqueue('e')
    sq.enqueue('f')
    assert len(sq) == 6
    assert sq.peek() == 'a'
    assert sq.dequeue() == 'a'
    assert sq.dequeue() == 'b'
    assert sq.dequeue() == 'c'
    assert sq.dequeue() == 'd'
    assert sq.dequeue() == 'e'
    assert sq.dequeue() == 'f'
    assert sq.peek() is None
    assert len(sq) == 0
