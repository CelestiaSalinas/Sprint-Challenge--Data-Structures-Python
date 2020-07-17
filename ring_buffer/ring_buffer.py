class RingBuffer:
    def __init__(self, capacity):
        self.max = capacity
        self.data = []


    class __Full:
        # class that implements a full buffer 
        def append(self, x):
            # Append an element overwriting the oldest one. 
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            # return list of elements in correct order 
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
       # append an element at the end of the buffer
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        # Return a list of elements from the oldest to the newest. 
        return self.data

#     buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']