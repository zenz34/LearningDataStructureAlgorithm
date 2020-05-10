# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sortedArrayToBST2(nums)

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        """
        LeetCode solution 2. Select right middle node as root.
        Same result as `sortedArrayToBST0()`.
        """

        def sorted_array_to_bst_helper(left, right):
            if left > right:
                return None

            # always choose right middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += 1

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = sorted_array_to_bst_helper(left, p - 1)
            root.right = sorted_array_to_bst_helper(p + 1, right)
            return root

        return sorted_array_to_bst_helper(0, len(nums) - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        """
        LeetCode solution 1. Select left middle node as root.
        """

        def sorted_array_to_bst_helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = sorted_array_to_bst_helper(left, p - 1)
            root.right = sorted_array_to_bst_helper(p + 1, right)
            return root

        return sorted_array_to_bst_helper(0, len(nums) - 1)

    def sortedArrayToBST0(self, nums: List[int]) -> TreeNode:
        def sorted_array_to_bst_helper(start, end):
            if start == end:
                return None

            middle_i = (start + end) // 2
            node = TreeNode(nums[middle_i])

            node.left = sorted_array_to_bst_helper(start, middle_i)
            node.right = sorted_array_to_bst_helper(middle_i + 1, end)

            return node

        return sorted_array_to_bst_helper(0, len(nums))
