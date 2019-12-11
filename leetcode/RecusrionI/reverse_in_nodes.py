# https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swapit(head, 2)

    def swapit(self, head, k):
        it = head
        for _ in range(k):
            if it:
                it = it.next
            else:
                return head

        prev = head
        curr = head.next

        for _ in range(k - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = self.swapit(curr, 2)
        return prev
