# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def mergeTwoLinkedLists(l1, l2):
    head = None
    pointer = None
    while l1 or l2:
        if l1 and l2:
            if l1.value <= l2.value:
                temp = ListNode(l1.value)
                l1 = l1.next
            else:
                temp = ListNode(l2.value)
                l2 = l2.next

        elif not l1 and l2:
            temp = ListNode(l2.value)
            l2 = l2.next
        else:
            temp = ListNode(l1.value)
            l1 = l1.next
        
        if head:
            pointer.next = temp
            pointer = pointer.next
        else:
            head = temp
            pointer = temp
                
    return head
