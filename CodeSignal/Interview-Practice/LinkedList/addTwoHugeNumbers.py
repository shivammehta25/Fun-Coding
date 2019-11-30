# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
        
def get_node_and_carry_from_sum(a, b, carry):
    c = a + b + carry
    num = c % 10000
    carry = c // 10000
    return carry, ListNode(num)

def print_list(a):
    if a:
        print(a.value)
        print_list(a.next)
    return None

def addTwoHugeNumbers(a, b):
    a = reverse_list(a)
    b = reverse_list(b)
    # print_list(a)
    head = None
    pointer = None
    carry = 0
    while a or b:
        if a:
            first_num = a.value
            a = a.next
        else:
            first_num = 0
            
        if b:
            second_num = b.value
            b = b.next
        else:
            second_num = 0
        
        carry, temp_node = get_node_and_carry_from_sum(first_num, second_num, carry)
        # print(carry, temp_node.value)
        if head:
            pointer.next = temp_node
            pointer = pointer.next
        else:
            head = temp_node
            pointer = temp_node
    
    if carry:
        pointer.next = ListNode(carry)
    
    return reverse_list(head)
