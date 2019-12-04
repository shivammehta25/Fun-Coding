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
    
    return prev, start, temp



def reverseNodesInKGroups(l, k):
    if not l or k == 1 or not l.next:
        return l
    
    iterator = l
    head = None
    prev_last_node = None
    
    current_start_node = l
    i = 0
    while iterator:
        i += 1
        if i % k != 0:
            iterator = iterator.next
        else:
            start, end, next_node = reverse_list_with_k(current_start_node, k)
            if head is None:
                head = start
                
            if prev_last_node:
                prev_last_node.next = start
            
            prev_last_node = end
                
            current_start_node = next_node
            iterator = next_node
            
    prev_last_node.next = current_start_node

    return head
            
