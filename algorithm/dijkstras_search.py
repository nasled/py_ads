from data_structure.priority_queue import PriorityQueue


class PriorityQueueDijkstra(PriorityQueue):
    def put(self, priority_tuple):
        (priority, value) = priority_tuple
        self.enqueue(priority, value)

    def get(self):
        index = min(self.queue.keys())
        if index in self.queue:
            if len(self.queue[index]) > 1:
                value = self.queue[index].pop(0)
            else:
                value = self.queue.pop(index)[0]
            return index, value
        else:
            return False

    def empty(self):
        return False if len(self.queue) else True

    def exists(self, priority_tuple):
        edge, node = priority_tuple
        if edge in self.queue:
            if node in self.queue[edge]:
                return True
        return False


if __name__ == "__main__":
    pqd = PriorityQueueDijkstra()
    pqd.put((0, "a"))
    pqd.put((2, "b"))
    pqd.put((1, "c"))
    pqd.put((1, "d"))
    assert pqd.exists((1, "c"))
    assert pqd.exists((0, "c")) is False
    assert pqd.get() == (0, "a")
    assert pqd.get() == (1, "c")
    assert pqd.get() == (1, "d")
    assert pqd.empty() is False
    assert pqd.get() == (2, "b")
    assert pqd.empty() is True


class Dijkstra:
    def __init__(self, edges):
        self.nodes_visited = set()
        self.nodes = set([x[0] for x in edges] + [x[1] for x in edges])
        self.edges = {}
        for node in self.nodes:
            self.edges.setdefault(node, {})
        for edge in edges:
            node_from, node_to, distance = edge
            self.edges[node_from][node_to] = distance
            self.edges[node_to][node_from] = distance

    def calculate(self, node_from, node_to):
        tentative_distances = dict()
        for node in self.nodes:
            if node is node_from:
                tentative_distances[node] = 0
            else:
                tentative_distances[node] = float('Infinity')

        queue = PriorityQueueDijkstra()
        queue.put((0, node_from))
        while not queue.empty():
            distance, current_node = queue.get()
            if current_node not in self.nodes_visited:
                for neighbor in self.edges[current_node]:
                    new_distance = tentative_distances[current_node] + self.edges[current_node][neighbor]
                    prev_distance = tentative_distances[neighbor]
                    if prev_distance > new_distance:
                        tentative_distances[neighbor] = new_distance
                        queue.put((new_distance, neighbor))
                self.nodes_visited.add(current_node)
        return tentative_distances[node_to]


if __name__ == "__main__":
    input_edges = [
        ("a", "b", 7),
        ("a", "c", 4),
        ("b", "c", 11),
        ("b", "d", 1),
        ("c", "d", 20),
        ("c", "f", 9),
        ("d", "e", 1),
        ("e", "f", 2),
        ("d", "g", 3),
        ("e", "g", 5),
        ("e", "h", 10),
        ("f", "h", 6),
        ("g", "i", 12),
        ("e", "i", 15),
        ("h", "i", 5)
    ]
    graph = Dijkstra(input_edges)
    assert graph.calculate("a", "i") == 22
