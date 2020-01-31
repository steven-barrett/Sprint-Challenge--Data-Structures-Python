import collections


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity-1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        results = []
        for item in self.storage:
            if item is not None:
                results.append(item)
        return results


buffer = RingBuffer(4)
buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)
buffer.append(5)
buffer.append(6)
print(buffer.get())
