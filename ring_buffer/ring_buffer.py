class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.size = 0
        self.oldest_index = 0

    def append(self, item):
        if self.size < self.capacity:
            # in this instance, the RingBuffer is NOT yet at max capacity
            self.data.append(item)
            self.size += 1
        else:
            # in this instance, the RingBuffer is at max capacity
            # remove oldest item from data
            self.data.pop(self.oldest_index)
            # insert item into data at oldest_item index
            self.data.insert(self.oldest_index, item)
            # change oldest index
            if self.oldest_index == self.capacity-1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1

    def get(self):
        return self.data