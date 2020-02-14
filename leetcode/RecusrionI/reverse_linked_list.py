# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode: 
        if not head or not head.next:
            return head
        
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None;
        return temp
