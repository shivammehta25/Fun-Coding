# https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    while l and l.value == k:
        l = l.next
    head = l
    while l and l.next:
        if l.next.value == k:
            l.next = l.next.next
        else:
            l = l.next
    
    return head
