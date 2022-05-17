from algorithm.bubble_sort import bubble_sort


class MinHeap:
    def __init__(self):
        self.count = 0
        self.heap_list = []

    def add(self, value):
        self.heap_list.append(value)
        self.count = self.count + 1
        self.min_heapify()

    def swap(self, value_from, value_to):
        index_from = self.heap_list.index(value_from)
        index_to = self.heap_list.index(value_to)
        self.heap_list[index_from] = value_to
        self.heap_list[index_to] = value_from

    def min_heapify(self):
        i = self.count - 1

        while i > 0 and self.heap_list[int((i-1)/2)] > self.heap_list[i]:
            self.swap(self.heap_list[i], self.heap_list[int((i-1)/2)])
            i = int((i - 1) / 2)

    def swap_by_index(self, index_from, index_to):
        value_from = self.heap_list[index_from]
        value_to = self.heap_list[index_to]
        self.heap_list[index_to] = value_from
        self.heap_list[index_from] = value_to

    def remove(self, value):
        if value in self.heap_list:
            value_index = self.heap_list.index(value)
            self.count = self.count - 1
            self.heap_list[value_index] = self.heap_list[self.count]
            self.heap_list = bubble_sort(self.heap_list)
            return True
        else:
            return False

    def contains(self, value):
        index = 0
        while index < self.count and self.heap_list[index] != value:
            index = index + 1
        return True if self.count > index else False

    def peek(self):
        return self.heap_list[0]


if __name__ == "__main__":
    h = MinHeap()
    h.add(5)
    assert h.peek() == 5
    h.add(4)
    assert h.peek() == 4
    h.add(3)
    assert h.peek() == 3
    h.add(2)
    assert h.peek() == 2
    h.add(1)
    assert h.peek() == 1
    assert h.count == 5
    assert h.remove(1) is True
    assert h.remove(1) is False
    assert h.count == 4
    assert h.peek() == 2

    h2 = MinHeap()
    h2.add(90)
    h2.add(100)
    h2.add(130)
    h2.add(140)
    h2.add(150)
    h2.remove(150)
    h2.remove(90)
    h2.remove(130)
    assert h2.count == 2
    assert h2.contains(100) is True
    h2.remove(100)
    assert h2.contains(100) is False
    h2.remove(140)
    assert h2.contains(140) is False
    assert h2.count == 0
