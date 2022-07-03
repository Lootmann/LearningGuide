class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    message: explanation of the error."""

    def __init__(self, message: str):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.
    """

    def __init__(self, message: str):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._buffer = [-1] * self._capacity

        # read pointer
        self.tail = 0

        # write pointer
        self.head = 0

    def _increment(self, val):
        return (val + 1) % self._capacity

    def read(self):
        if self._buffer[self.tail] == -1:
            raise BufferEmptyException("Circular buffer is empty")

        top = self._buffer[self.tail]
        self._buffer[self.tail] = -1
        self.tail = self._increment(self.tail)
        return top

    def write(self, data):
        if self._buffer[self.head] != -1:
            raise BufferFullException("Circular buffer is full")

        self._buffer[self.head] = data
        self.head = self._increment(self.head)

    def overwrite(self, data):
        if self._buffer[self.head] == -1:
            self.write(data)
        else:
            self._buffer[self.head] = data
            self.tail = self._increment(self.tail)

        self.head = self._increment(self.head)

    def clear(self):
        self._buffer = [-1] * self._capacity
        self.tail = 0
        self.head = 0
