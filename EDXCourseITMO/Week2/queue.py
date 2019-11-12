class Queue:

    def __init__(self, maxlength):
        self.q = [None] * (maxlength + 1)
        self.tail = 0
        self.head = 0
        self.length = 0
        self.maxlength = maxlength

    def add(self, x):
        try:
            if self.head == self.maxlength:
                raise OverflowError
            self.q[self.tail] = x
            self.tail += 1
            self.length += 1
        except OverflowError as e:
            print(f'Overflow of Queue {e}')

    def deque(self):
        try:
            if self.tail == self.head:
                raise OverflowError
            self.length -= 1
            element = self.q[self.head]
            self.head += 1
            return element
        except OverflowError as e:
            print(f'Underflor Of Queue {e}')

    def __len__(self):
        return self.length


out = open('output.txt', 'w')
with open('input.txt', 'r') as input:
    maxlen = int(input.readline())
    queue = Queue(maxlen)
    for line in input:
        line = line.split()
        if len(line) > 1:
            queue.add(int(line[1]))
        else:
            out.write(str(queue.deque()) + '\n')

out.close()
