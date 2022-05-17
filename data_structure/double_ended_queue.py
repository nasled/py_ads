from standard_queue import StandardQueue


class DoubleEndedQueue(StandardQueue):
    def enqueueBack(self, value):
        return self.enqueue(value)

    def dequeueFront(self):
        return self.dequeue()

    def peekFront(self):
        return self.peek()

    def enqueueFront(self, value):
        return self.queue.insert(0, value)

    def dequeueBack(self):
        return self.queue.pop()

    def peekBack(self):
        if len(self.queue):
            return self.queue[-1]
        else:
            return None


if __name__ == "__main__":
    deq = DoubleEndedQueue()
    deq.enqueueBack('a')
    deq.enqueueBack('b')
    deq.enqueueBack('c')
    deq.enqueueBack('d')
    deq.enqueueBack('e')
    deq.enqueueBack('f')
    assert len(deq) == 6
    assert deq.peekFront() == 'a'
    assert deq.dequeueFront() == 'a'
    assert deq.dequeueFront() == 'b'
    assert deq.dequeueFront() == 'c'
    assert deq.dequeueFront() == 'd'
    assert deq.dequeueFront() == 'e'
    assert deq.dequeueFront() == 'f'
    assert deq.peekFront() is None
    assert len(deq) == 0
    deq.enqueueFront('a')
    deq.enqueueFront('b')
    deq.enqueueFront('c')
    assert len(deq) == 3
    assert deq.peekBack() == 'a'
    assert deq.peekFront() == 'c'
    assert deq.dequeueBack() == 'a'
    assert deq.dequeueBack() == 'b'
    assert len(deq) == 1
    assert deq.peekBack() == 'c'
