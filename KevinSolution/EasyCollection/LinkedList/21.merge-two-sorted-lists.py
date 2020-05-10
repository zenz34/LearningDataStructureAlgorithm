# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.mergeTwoLists6(l1, l2)

    def mergeTwoLists6(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Tail recursive.
        """
        
        def merge_two_lists_helper(l1: ListNode, l2: ListNode, prev):
            if l1 is None:
                prev.next = l2
            elif l2 is None:
                prev.next = l1
            elif l1.val < l2.val:
                prev.next = l1
                merge_two_lists_helper(l1.next, l2, prev.next)
            else:
                prev.next = l2
                merge_two_lists_helper(l1, l2.next, prev.next)

        prehead = ListNode(None)
        merge_two_lists_helper(l1, l2, prehead)
        return prehead.next
    
    def mergeTwoLists5(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        LeetCode solution 1.
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists4(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        LeetCode solution 2.
        """
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(None)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        # prev.next = l1 if l1 is not None else l2
        prev.next = l1 or l2

        return prehead.next

    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Broken because if `l2` has more to insert at the end, `l1` is `None` and can't
        insert into `None.next` and don't have previous node.
        Same as `mergeTwoLists2()` but don't track previous `l1` node to insert.
        """
        # Kinda annoying to have to check for `None` now so can access `.val`.
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1

        head = l1
        while l1 is not None and l2 is not None:
            if l2.val < l1.val:
                # Swap values to make `l1.val` less
                l1.val, l2.val = l2.val, l1.val
                # Insert l2 into l1 and advance l2.
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            else: # By doing swap in beginning, this `else:` happens more at start.
                l1 = l1.next
        # Can also do `if l1 is None:`.
        # Just checks that `l2` has elements left which also means
        # `l1` elements were all consumed.
        if l2 is not None:
            # Breaks here because `l1 is None` so `l1.next` will have `None` access error.
            # No way to append to `l1` besides O(n) looping through `l1` to find the previous
            # node before `None` and then append.
            l1.next = l2
        return head

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Same as `mergeTwoLists1()` but don't need `dummy_head` if make `l1` always smaller.
        Guarantees that no need to prepend from `l2` to `l1`.
        """
        # Kinda annoying to have to check for `None` now so can access `.val`.
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1

        head = l1
        while l1.next is not None and l2 is not None:
            if l2.val < l1.next.val:
                # Insert l2 into l1 and advance l2.
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            else: # By doing swap in beginning, this `else:` happens more at start.
                l1 = l1.next
        # Can also do `if l1.next is None:`.
        # Just checks that `l2` has elements left which also means
        # `l1` elements were all consumed.
        if l2 is not None:
            l1.next = l2
        return head
    
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Same as `mergeTwoLists0()` but swap in beginning to have less inserts at start.
        """
        # Kinda annoying to have to check for `None` now so can access `.val`.
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1

        dummy_head = ListNode(None)
        dummy_head.next = l1
        l1 = dummy_head
        while l1.next is not None and l2 is not None:
            if l2.val < l1.next.val:
                # Insert l2 into l1 and advance l2.
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            else: # By doing swap in beginning, this `else:` happens more at start.
                l1 = l1.next
        # Can also do `if l1.next is None:`.
        # Just checks that `l2` has elements left which also means
        # `l1` elements were all consumed.
        if l2 is not None:
            l1.next = l2
        return dummy_head.next
    
    def mergeTwoLists0(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Insertion merge into `l1`.
        """

        dummy_head = ListNode(None)
        dummy_head.next = l1
        l1 = dummy_head
        # while l1.next and l2:
        while l1.next is not None and l2 is not None:
            if l2.val < l1.next.val:
                # Insert l2 into l1 and advance l2.
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            else:
                l1 = l1.next
        # Can also do `if l1.next is None:`.
        # Just checks that `l2` has elements left which also means
        # `l1` elements were all consumed.
        if l2 is not None:
            l1.next = l2
        return dummy_head.next
