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
    while i < k and head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        i += 1
        
    if i < k:
        prev, start, temp = reverse_list_with_k(prev, i)
    
    return prev, start, temp



def reverseNodesInKGroups(l, k):
    if not l or k == 1 or not l.next:
        return l
    
    iterator = l
    head = None
    prev_last_node = None
    

    while iterator:
        start, end, next_node = reverse_list_with_k(iterator, k)
        print(f'start: {start.value}, end: {end.value}')
        if head is None:
            head = start
        
        if prev_last_node:
            print(f'Prev node: {prev_last_node.value}')
            prev_last_node.next = start
        
        
        prev_last_node = end
        
        
        iterator = next_node

    prev_last_node.next = iterator

    return head
            
