from collections import deque
from itertools import chain
from operator import attrgetter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.levelOrder4(root)

    def levelOrder4(self, root: TreeNode) -> List[List[int]]:
        """
        fifo BFS LeetCode solution 2 modified.
        No need to keep track of the level like LeetCode does since
        can just append or get last list.
        LeetCode doesn't put `None` in `fifo`. This helps skip levels that
        are empty ie. all `None`, but need to pre-check outside loop and children.
        Putting `None` in `fifo` requires checking for empty `level_node_vals`.
        """

        level_order_node_vals = []
        fifo = deque((root,))

        while fifo:
            level_node_vals = []

            for _ in range(len(fifo)):
                node = fifo.popleft()

                if node is not None:
                    level_node_vals.append(node.val)
                    fifo.append(node.left)
                    fifo.append(node.right)

            if level_node_vals:
                level_order_node_vals.append(level_node_vals)

        return level_order_node_vals

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """
        Same as `levelOrder2` but use closure variable for `level_order_node_vals`.
        """

        level_order_node_vals = []

        def level_order_helper(node, level):
            if node is None:
                return

            if level == len(level_order_node_vals):
                level_order_node_vals.append([])

            level_order_node_vals[level].append(node.val)

            level_order_helper(node.left, level + 1)
            level_order_helper(node.right, level + 1)

        level_order_helper(root, 0)
        return level_order_node_vals

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        LeetCode solution 1 modified.
        Preorder DFS adding/appending to `level_order_node_vals`.
        Use preorder over postorder or inorder because it discovers
        new levels in order so can just append one level list at a time without
        jumping.
        """

        def level_order_helper(node, level, level_order_node_vals):
            if node is None:
                return level_order_node_vals

            if level == len(level_order_node_vals):
                level_order_node_vals.append([])

            level_order_node_vals[level].append(node.val)

            level_order_helper(node.left, level + 1, level_order_node_vals)
            level_order_helper(node.right, level + 1, level_order_node_vals)

            return level_order_node_vals

        return level_order_helper(root, 0, [])

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """
        fifo BFS without iterators.
        """

        level_order_node_vals = []
        fifo = deque(((root,),))

        while fifo:
            fifo_nodes = fifo.popleft()

            level_node_vals = []
            next_fifo_nodes = []
            for node in fifo_nodes:
                if node is not None:
                    level_node_vals.append(node.val)
                    next_fifo_nodes.append(node.left)
                    next_fifo_nodes.append(node.right)

            if level_node_vals:
                level_order_node_vals.append(level_node_vals)
                fifo.append(next_fifo_nodes)

        return level_order_node_vals

    def levelOrder0(self, root: TreeNode) -> List[List[int]]:
        """
        fifo BFS with iterators.
        """

        level_order_node_vals = []
        fifo = deque(((root,),))

        identity = lambda x: x
        get_val = attrgetter('val')
        get_children = attrgetter('left', 'right')
        while fifo:
            fifo_nodes = fifo.popleft()
            level_nodes = tuple(filter(identity, fifo_nodes))

            level_node_vals = tuple(map(get_val, level_nodes))
            if level_node_vals:
                level_order_node_vals.append(level_node_vals)
                next_fifo_nodes = tuple(chain.from_iterable(map(get_children, level_nodes)))
                fifo.append(next_fifo_nodes)

        return level_order_node_vals
