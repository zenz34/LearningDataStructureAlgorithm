# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.removeNthFromEnd1(head, n)
    
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(None)
        slow = dummy_head
        slow.next = head
        fast = dummy_head
        for _ in range(n):
            fast = fast.next
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy_head.next

    def removeNthFromEnd0(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = slow
        for _ in range(n):
            fast = fast.next
            
        if fast is None:
            return slow.next
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head
