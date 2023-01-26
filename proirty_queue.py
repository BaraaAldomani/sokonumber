import heapq

class PriorityQueue:
    """Define a PriorityQueue data structure that will be used"""
    def  __init__(self):
        self.Heap = []

    def push(self, priority, item):
        entry = (priority, item)
        heapq.heappush(self.Heap, entry)

    def pop(self):
        (priority, node) = heapq.heappop(self.Heap)
        print((priority, node))
        print(node)
        return node

    def isEmpty(self):
        return len(self.Heap) == 0