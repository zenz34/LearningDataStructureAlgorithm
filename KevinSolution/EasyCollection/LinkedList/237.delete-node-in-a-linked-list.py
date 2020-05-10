# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        self.deleteNode4(node)
        
    def deleteNode4(self, node):
        """
        LeetCode solution.
        """
        node.val = node.next.val
        node.next = node.next.next

    def deleteNode3(self, node):
        curr_node = node
        next_node = node.next
        while next_node is not None:
            curr_node.val = next_node.val
            if next_node.next is None:
                curr_node.next = None
                next_node = None
            else:
                curr_node = next_node
                next_node = next_node.next

    def deleteNode2(self, node):
        curr_node = node
        next_node = node.next
        while next_node.next is not None:
            curr_node.val = next_node.val
            curr_node = next_node
            next_node = next_node.next
        curr_node.val = next_node.val
        curr_node.next = None

    def deleteNode1(self, node):
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            else:
                node = node.next

    def deleteNode0(self, node):
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
