# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.swapit(head, k)

    def swapit(self, head, k):
        it = head
        for _ in range(k):
            if it:
                it = it.next
            else:
                return head
        if head is None:
            return None
        prev = head
        curr = head.next
        for _ in range(k - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = self.swapit(curr, k)
        return prev
