from collections import deque


class Queue:

    def __init__(self, max_len):
        self._queue = deque(maxlen=max_len)

    def enqueue(self, x):
        self._queue.appendleft(x)

    def dequeue(self):
        return self._queue.pop()



out = open('output.txt', 'w')
with open('input.txt', 'r') as input:
    maxlen = int(input.readline())
    q = Queue(maxlen)
    for line in input:
        line = line.split()
        if len(line) > 1:
            q.enqueue(int(line[1]))
        else:
            out.write(str(q.dequeue()) + '\n')

out.close()
