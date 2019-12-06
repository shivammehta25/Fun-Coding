# https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt/solutions
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(head, n):
    if n < 1:
        return head
    
    l = 0
    iterator = head
    while iterator:
        iterator = iterator.next
        l += 1

    if l <= 1 or n >= l:
        return head

    reversing_elements = l - n
    
    i = 0
    start = head
    while head:
        i += 1
        if i == reversing_elements:
            new_head = head.next
            head.next = None
            head = new_head
        if head.next:
            head = head.next
        else:
            break
    
    head.next = start
    
    return new_head
