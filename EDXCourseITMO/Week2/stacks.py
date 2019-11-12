class Stack:
    def __init__(self):
        self.stack = []
        self.length = -1

    def push(self, x):
        self.stack.append(x)
        self.length += 1

    def pop(self):
        element = self.stack[self.length]
        del self.stack[self.length]
        self.length -= 1
        return element

    def __len__(self):
        print(self.length)


out = open('output.txt', 'w')
with open('input.txt', 'r') as input:
    stack = Stack()
    input.readline()
    for line in input:
        line = line.split()
        if len(line) > 1:
            stack.push(int(line[1]))
        else:
            out.write(str(stack.pop()) + '\n')

out.close()
