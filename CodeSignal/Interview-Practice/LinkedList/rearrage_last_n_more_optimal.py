# https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt/description
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(head, n):
    if n < 1:
        return head
    
    first = head
    second = head
    
    for _ in range(n):
        if first.next:
            first = first.next
        else:
            return head
    
    while first and first.next:
        first = first.next
        second = second.next
    if first:
        first.next = head
        new_head = second.next
        second.next = None

    
    return new_head
