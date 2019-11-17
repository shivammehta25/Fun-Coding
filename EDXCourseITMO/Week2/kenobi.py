# Implementation Try with Doubly Linked List

class DoubleLinkedList:

    class Node:
        def __init__(self,x=None):
            self.x = x
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.middle = self.head
        self.length = 0

    def add(self, x):
        new_node = self.Node(x)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.length += 1
        if self.length %2 == 0:
            self.middle = self.middle.next

    def remove(self):
        if self.length == 0:
            return -1

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.length -= 1
        if self.length % 2 != 0:
            self.middle = self.middle.prev

    def printfwd(self, iterator=None, till=None):
        if not iterator:
            iterator = self.head.next
        else:
            iterator = iterator.next
        result = []
        while iterator.next:
            result.append(str(iterator.x))
            if till:
                if till.x == iterator.x:
                    break
            iterator = iterator.next
        return result

    def printbwd(self, iterator=None, till=None):
        if not iterator:
            iterator = self.tail.prev
        else:
            iterator = iterator.prev
        result = []
        while iterator.prev:
            if till:
                if till.x == iterator.x:
                    break
            result.append(str(iterator.x))
            iterator = iterator.prev
        return result

    def mum(self):
        print(self.head.next.x, self.middle.x)
        temp = self.head
        self.head = self.middle
        self.middle = temp
        print(self.head.next.x, self.middle.x)

out = open('output.txt', 'w')
with open('input.txt') as inp:
    dll = DoubleLinkedList()
    n = int(inp.readline())
    for i in range(n):
        line = inp.readline().split()
        if line[0].lower() == 'add':
            dll.add(int(line[1]))
        elif line[0].lower() == 'take':
            dll.remove()
        else:
            dll.mum()

    out.writelines(str(dll.length) + '\n')
    out.writelines(' '.join(dll.printfwd(dll.middle)))
    if dll.length > 1:
        out.writelines(' ')
        out.writelines(' '.join(dll.printfwd(None, dll.middle)))
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
