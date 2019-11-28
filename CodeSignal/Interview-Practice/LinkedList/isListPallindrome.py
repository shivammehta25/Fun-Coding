# https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4
def get_len_and_mid(head):
    slow_ptr = head
    fast_ptr = head
    length = 0
    while fast_ptr and fast_ptr.next:
        length += 1
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    middle_ptr = slow_ptr
    while slow_ptr:
        length += 1
        slow_ptr = slow_ptr.next

    return length, middle_ptr
 

def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def isListPalindrome(l):
    ll, middle_p = get_len_and_mid(l)
    if ll % 2 != 0:
        middle_p = middle_p.next

    reverse_list = reverse(middle_p)
    i = 0
    print(ll)
    while i < ll//2:
        if l.value == reverse_list.value:
            i += 1
            l = l.next
            reverse_list = reverse_list.next
            continue
        return False
    
    return True
