from data_structure.standard_queue import StandardQueue


class PriorityQueue(StandardQueue):
    def __init__(self):
        self.queue = {}

    def enqueue(self, priority, value):
        if type(priority) != int:
            return False
        if priority not in self.queue:
            self.queue[priority] = []
        self.queue[priority].append(value)
        return True

    def dequeue(self):
        index = min(self.queue.keys())
        if index in self.queue:
            return self.queue.pop(index)
        else:
            return False

    def peek(self):
        index = min(self.queue.keys())
        if index in self.queue:
            return self.queue.get(index)
        else:
            return False


if __name__ == "__main__":
    deq = PriorityQueue()
    deq.enqueue(5, 'a')
    deq.enqueue(3, 'b')
    deq.enqueue(7, 'c')
    deq.enqueue(9, 'd')
    deq.enqueue(6, 'e')
    assert deq.peek() == ['b']
    deq.dequeue()
    deq.dequeue()
    assert deq.peek() == ['e']
