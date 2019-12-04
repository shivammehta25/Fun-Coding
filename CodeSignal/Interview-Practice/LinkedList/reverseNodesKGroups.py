# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverse_list_with_k(head, k):
    i = 0
    start = head
    prev = None
    print('Reversse start: {}'.format(start.value))
    while i < k and head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        i += 1
    print('reversed start, prev: {} {}'.format(start.value, prev.value))
    return prev, start

def reverseNodesInKGroups(l, k):
    if not l or k == 1 or not l.next:
        return l
    
    iterator = l
    head = None
    i = 0 
    prev_last_node = None
    while iterator:
        i += 1
        if i % k != 0:
            iterator = iterator.next

        else:
            temp = iterator.next
            print(iterator.value)
            start, end = reverse_list_with_k(iterator, k)
            print(start.value)
            if i != k:
                prev_last_node.next = start

            if head is None:
                print('here')

                head = start
            
            prev_last_node = end
            iterator = temp
            
    
    return head
            
