# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        Iterative solution. Reverse pointers.
        """
        if head is None or head.next is None:
            return head

        slow = head
        fast = slow.next
        slow.next = None
        while fast is not None:
            next_fast = fast.next
            fast.next = slow
            slow = fast
            fast = next_fast
            
        return slow

    def reverseList1(self, head: ListNode) -> ListNode:
        def reverse_list_helper(head):
            """
            Fast recursive solution.
            Reverse rest and then fix pointers on `head` and `tail`.
            """
            if head is None or head.next is None:
                return head
            tail = head.next
            reversed_head = reverse_list_helper(head.next)
            tail.next = head
            head.next = None
            return reversed_head
        
        return reverse_list_helper(head)

    def reverseList0(self, head: ListNode) -> ListNode:
        """
        Slow recursive solution.
        1 2 3 4 5
        Reverse rest
        1 5 4 3 2
        swap head tail
        5 1 4 3 2
        reverse back next rest
        5 1 2 3 4
        reverse rest
        5 4 3 2 1
        """
        def reverse_list_helper(head):
            if head is None or head.next is None:
                return head
            reverse_list_helper(head.next)
            head.val, head.next.val = head.next.val, head.val
            reverse_list_helper(head.next.next)
            reverse_list_helper(head.next)
            return head
        
        return reverse_list_helper(head)
