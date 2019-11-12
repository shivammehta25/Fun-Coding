import math


class MinQueue:

    def __init__(self, maxlength):
        self.q_f = []
        self.q_b = []
        self.maxlength = maxlength
        self.min_value = math.inf
        self.length = 0

    def add(self, x):
        print('Added: ', x)
        self.q_f.append(x)
        self.length += 1
        self.min_value = min(x, self.min_value)
        print(self.min_value)

    def deque(self):
        self.length -= 1
        if not self.q_b:
            self.q_b.append(self.q_f.pop())
            while self.q_f:
                self.q_b.append(min(self.q_b[-1], self.q_f.pop()))
            self.min_value = math.inf
        element = self.q_b.pop()
        print('Popping: ', element)
        print(self.min_value)
        return element

    def check_min(self):
        res = self.min_value
        if self.q_b:
            return min(res, self.q_b[-1])
        return res

    def __len__(self):
        return self.length


out = open('output.txt', 'w')
with open('input.txt', 'r') as input:
    maxlen = int(input.readline())
    queue = MinQueue(maxlen)
    for line in input:
        line = line.split()
        if len(line) > 1:
            queue.add(int(line[1]))
        else:
            if str(line[0]) != '-':
                out.write(str(queue.check_min()) + '\n')
            else:
                queue.deque()

out.close()
