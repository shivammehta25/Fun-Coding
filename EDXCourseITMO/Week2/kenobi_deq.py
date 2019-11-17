# Implementation Try with Doubly Linked List
from collections import deque

class Kenobi:
    def __init__(self):
        self.a = deque()
        self.b = deque()

    def add(self,x ):
        self.a.append(x)

    def remove(self):
        if self.a:
            self.a.pop()
        else:
            self.b.popleft()

    def mums(self):
        t = deque(self.a)
        self.a = self.b
        self.b = t
        
    def balance(self):
        if len(self.a) > len(self.b):
            self.b.appendleft(self.a.popleft())
        elif len(self.a) < len(self.a):
            self.a.add(self.b.popleft())


out = open('output.txt', 'w')
with open('input.txt') as inp:
    dll = Kenobi()
    n = int(inp.readline())
    for i in range(n):
        line = inp.readline().split()
        if line[0].lower() == 'add':
            dll.add(line[1])
        elif line[0].lower() == 'take':
            dll.remove()
        else:
            dll.mums()
        dll.balance()
        print(dll.a, dll.b)
    while dll.a:
        dll.b.append(dll.a.pop())
    out.writelines(str(len(dll.b)) + '\n')
    out.writelines(' '.join(dll.b))
    
    out.writelines('\n')
    
    
out.close()



# Test Cases for implementation
# if __name__ == '__main__':
#     dll = DoubleLinkedList()
#     dll.add(1)
#     dll.add(2)
#     dll.add(3)
#     dll.printfwd()
#     print(f'Middle: {dll.middle.x}')
#     dll.add(4)
#     dll.add(5)
#     dll.add(6)
#     print(f'Middle: {dll.middle.x}')
#     print('Forward Print:')
#     dll.printfwd()
#     print('Backward Print:')
#     dll.printbwd()
#     dll.remove()
#     print(f'Middle: {dll.middle.x}')
#     dll.printfwd()
