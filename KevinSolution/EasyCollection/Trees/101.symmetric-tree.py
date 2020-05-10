from collections import deque
from itertools import islice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetric5(root)

    def isSymmetric5(self, root: TreeNode) -> bool:
        """
        LeetCode solution 2 modified.
        """
        fifo = deque(((root, root),))

        while fifo:
            node0, node1 = fifo.pop()
            if node0 is node1 is None:
                continue
            elif node0 is None or node1 is None:
                return False
            # node0 is not None and node1 is not None:
            elif node0.val != node1.val:
                return False

            fifo.append((node0.left, node1.right))
            fifo.append((node0.right, node1.left))

        return True

    def isSymmetric4(self, root: TreeNode) -> bool:
        """
        LeetCode solution 2.
        """
        fifo = deque((root, root))

        while fifo:
            node0 = fifo.popleft()
            node1 = fifo.popleft()
            if node0 is node1 is None:
                continue
            elif node0 is None or node1 is None:
                return False
            # node0 is not None and node1 is not None:
            elif node0.val != node1.val:
                return False
            fifo.append(node0.left)
            fifo.append(node1.right)

            fifo.append(node0.right)
            fifo.append(node1.left)

        return True

    def isSymmetric3(self, root: TreeNode) -> bool:
        """
        BFS and check each level is a palindrome.
        Slow because duplicate work for add and palindrome check.
        Also extra work for adding in `None`.
        """
        fifo = deque((root,))
        level_nodes_length = 1

        while True:
            level_nodes = [fifo.popleft() for _ in range(level_nodes_length)]
            if not type(self).is_palindrome1(level_nodes):
                return False

            level_nodes_length = 0
            all_next_level_nodes_none = True

            for node in level_nodes:
                left = None
                right = None

                if node is not None:
                    left = node.left
                    right = node.right

                if left is not None or right is not None:
                    all_next_level_nodes_none = False

                fifo.append(left)
                level_nodes_length += 1
                fifo.append(right)
                level_nodes_length += 1

            if all_next_level_nodes_none:
                break

        return True

    @classmethod
    def is_palindrome1(cls, nodes: List) -> bool:
        get_node_value = lambda node: None if node is None else node.val

        i = 0
        j = len(nodes) - 1

        while i < j:
            node_values = map(get_node_value, (nodes[i], nodes[j]))
            if not cls.are_node_values_equal(*node_values):
                return False
            i += 1
            j -= 1

        return True

    @classmethod
    def is_palindrome0(cls, nodes: List) -> bool:
        get_node_value = lambda node: None if node is None else node.val
        node_values = map(get_node_value, nodes)
        reversed_node_values = map(get_node_value, reversed(nodes))

        node_values_pairwise_equal = map(
            cls.are_node_values_equal,
            node_values,
            reversed_node_values
        )

        node_values_pairwise_half_equal = islice(
            node_values_pairwise_equal,
            0,
            len(nodes) // 2
        )
        return all(node_values_pairwise_half_equal)

    @staticmethod
    def are_node_values_equal(value0, value1):
        return (
            # Should use `is` to compare `None` in case `.val` is custom class.
            # https://stackoverflow.com/a/14247383/7381355
            # Don't use `x is y` without `None` because equal identity doesn't imply
            # equality depending on class implementation.
            value0 is value1 is None or
            value0 == value1
        )

    def isSymmetric2(self, root: TreeNode) -> bool:
        """
        LeetCode solution 1.
        """

        def is_mirror(root0, root1) -> bool:
            if root0 is root1 is None:
                return True
            elif root0 is None or root1 is None:
                return False
            # root0 is not None and root1 is not None:
            return (
                root0.val == root1.val and
                is_mirror(root0.left, root1.right) and
                is_mirror(root0.right, root1.left)
            )

        return is_mirror(root, root)

    def isSymmetric1(self, root: TreeNode) -> bool:
        """
        Self-programmed LeetCode solution 1.
        """

        def is_symmetric_helper(node0, node1) -> bool:
            if node0 is node1 is None:
                return True
            elif node0 is None:
                return False
            elif node1 is None:
                return False
            else: # node0 is not None and node1 is not None:
                return (
                    node0.val == node1.val and
                    is_symmetric_helper(node0.left, node1.right) and
                    is_symmetric_helper(node0.right, node1.left)
                )

        return is_symmetric_helper(root, root)

    def isSymmetric0(self, root: TreeNode) -> bool:
        """
        Recursive generator preorder comparison.
        """

        if root is None:
            return True

        def generate_preorder_left_traversal(root: TreeNode) -> bool:
            if root is None:
                yield None
                return
            yield root.val
            # Python 2.7 alternative:
            # for val in generate_preorder_left_traversal(root.left):
            #     yield value
            yield from generate_preorder_left_traversal(root.left)
            yield from generate_preorder_left_traversal(root.right)

        def generate_preorder_right_traversal(root: TreeNode) -> bool:
            if root is None:
                yield None
                return
            yield root.val
            # Python 2.7 alternative:
            # for val in generate_preorder_left_traversal(root.left):
            #     yield value
            yield from generate_preorder_right_traversal(root.right)
            yield from generate_preorder_right_traversal(root.left)

        return all(map(
            type(self).are_node_values_equal,
            generate_preorder_left_traversal(root.left),
            generate_preorder_right_traversal(root.right)
        ))
