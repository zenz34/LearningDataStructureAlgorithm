# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepth4(root)

    def maxDepth4(self, root: TreeNode) -> int:
        """
        Iterative stack version of `maxDepth0()` with double recursive calls at end
        translated to double append to stack.
        """

        lifo = [(root, 0)]

        max_depth = -float('inf')

        while lifo:
            node, depth = lifo.pop()

            max_depth = max(max_depth, depth)

            if node is not None:
                lifo.append((node.left, depth + 1))
                lifo.append((node.right, depth + 1))
                
        return max_depth

    def maxDepth3(self, root: TreeNode) -> int:
        """
        LeetCode solution 1. No argument accumulator.
        """

        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        def max_depth_helper(node: TreeNode, level):
            """
            Not using `None` as end marker. Check "next" `.left` and `.right`.
            """

            if node.left is None and node.right is None:
                return level

            left_max_level = -float('inf')
            if node.left is not None:
                left_max_level = max_depth_helper(node.left, level + 1)
            right_max_level = -float('inf')
            if node.right is not None:
                right_max_level = max_depth_helper(node.right, level + 1)

            return max(
                left_max_level,
                right_max_level
            )

        return 0 if root is None else max_depth_helper(root, 1)

    def maxDepth1(self, root: TreeNode) -> int:
        def max_depth_helper(node: TreeNode, level):
            """
            Not using `None` as end marker. Check "next" `.left` and `.right`.
            """

            if node.left is None and node.right is None:
                return level
            elif node.left is not None and node.right is not None:
                return max(
                    max_depth_helper(node.left, level + 1),
                    max_depth_helper(node.right, level + 1)
                )
            elif node.left is not None:
                return max_depth_helper(node.left, level + 1)
            elif node.right is not None:
                return max_depth_helper(node.right, level + 1)

        return 0 if root is None else max_depth_helper(root, 1)

    def maxDepth0(self, root: TreeNode) -> int:
        """
        Using `None` as end marker.
        """

        def max_depth_helper(node: TreeNode, depth):
            if node is None:
                return depth

            return max(
                max_depth_helper(node.left, depth + 1),
                max_depth_helper(node.right, depth + 1)
            )

        return max_depth_helper(root, 0)
