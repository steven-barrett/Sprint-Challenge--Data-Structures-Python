import collections


class Ring_Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = collections.OrderedDict()

    def append(self, item):
        try:
            self.current += 1
            self.storage.pop(item)
        except KeyError:
            if len(self.storage) >= self.capacity:
                self.storage.popitem(last=False)
                self.current = self.capacity
        self.storage[item] = item

    def get(self):
        items = []
        try:
            for item in self.storage:
                if not item == None:
                    items.append(item)
            return items
        except KeyError:
            return None


buffer = Ring_Buffer(4)
buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)
buffer.append(5)
buffer.append(6)
print(buffer.get())
