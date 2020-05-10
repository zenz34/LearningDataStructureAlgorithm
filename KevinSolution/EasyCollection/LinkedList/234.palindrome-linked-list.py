# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.isPalindrome0(head)
    
    def isPalindrome0(self, head: ListNode) -> bool:
        middle_node = self.find_middle_node(head)
        reversed_second_half = self.reverseList(middle_node)
        return self.list_equals(head, reversed_second_half)

    def list_equals(self, x, y):
        while x is not None and y is not None:
            if x.val != y.val:
                return False
            x = x.next
            y = y.next
        return True
        
    def find_middle_node(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseList3(head)

    def reverseList3(self, head: ListNode) -> ListNode:
        """
        Iterative solution. Reverse pointers.
        """
        if head is None or head.next is None:
            return head

        prev_node = head
        curr_node = prev_node.next
        prev_node.next = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node
