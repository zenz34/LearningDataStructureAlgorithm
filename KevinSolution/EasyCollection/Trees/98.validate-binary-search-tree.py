# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST8(root)

    def isValidBST8(self, root):
        """
        LeetCode solution 3. Inorder iterative traversal.
        Use `root` to queue next right node to left expand.

        For postorder:
        Reverse right-favored preorder.
        https://www.geeksforgeeks.org/iterative-postorder-traversal/
        Left expansion but favor right queue before visiting current.
        https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
        """

        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

    def isValidBST7(self, root):
        """
        LeetCode solution 3 modified.
        """
        stack, current_max = [root], float('-inf')

        while stack:
            node = stack.pop()
            while node:
                stack.append(node)
                node = node.left

            if not stack:
                break

            node = stack.pop()

            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if node.val <= current_max:
                return False
            current_max = node.val

            stack.append(node.right)

        return True

    def isValidBST6(self, root: TreeNode) -> bool:
        """
        DFS inorder traversal.
        """

        current_max = -float('inf')
        def is_valid_bst_helper(node):
            nonlocal current_max

            return (
                node is None or
                is_valid_bst_helper(node.left) and
                current_max < node.val and
                ((current_max := node.val) or True) and
                is_valid_bst_helper(node.right)
            )

        return is_valid_bst_helper(root)

    def isValidBST5(self, root: TreeNode) -> bool:
        """
        DFS inorder traversal.
        """

        current_max = -float('inf')
        def is_valid_bst_helper(node):
            nonlocal current_max

            if node is None:
                return True

            if not is_valid_bst_helper(node.left):
                return False

            if node.val <= current_max:
                return False
            else:
                current_max = node.val

            if not is_valid_bst_helper(node.right):
                return False

            return True

        return is_valid_bst_helper(root)

    def isValidBST4(self, root: TreeNode) -> bool:
        """
        Recursive range with no `and` combine from parent and boxed variable.
        """

        def is_valid_bst_helper(node, lower_limit, upper_limit, is_valid_bst_box):
            if not is_valid_bst[0] or node is None:
                return

            if not (lower_limit < node.val < upper_limit):
                is_valid_bst[0] = False
                return

            is_valid_bst_helper(node.left, lower_limit, node.val, is_valid_bst_box)
            is_valid_bst_helper(node.right, node.val, upper_limit, is_valid_bst_box)

            return is_valid_bst_box[0]

        return is_valid_bst_helper(root, -float('inf'), float('inf'), [True])

    def isValidBST3(self, root: TreeNode) -> bool:
        """
        Recursive range with no `and` combine from parent and closure variable.
        """

        is_valid_bst = True

        def is_valid_bst_helper(node, lower_limit, upper_limit):
            nonlocal is_valid_bst

            if not is_valid_bst or node is None:
                return

            if not (lower_limit < node.val < upper_limit):
                is_valid_bst = False
                return

            is_valid_bst_helper(node.left, lower_limit, node.val)
            is_valid_bst_helper(node.right, node.val, upper_limit)

        is_valid_bst_helper(root, -float('inf'), float('inf'))
        return is_valid_bst

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        Iterative range.
        LeetCode solution 2.
        """

        lifo = [(root, -float('inf'), float('inf'))]

        while lifo:
            node, lower_limit, upper_limit = lifo.pop()

            if node is None:
                continue

            if not (lower_limit < node.val < upper_limit):
                return False

            lifo.append((node.left, lower_limit, node.val))
            lifo.append((node.right, node.val, upper_limit))

        return True

    def isValidBST1(self, root: TreeNode) -> bool:
        """
        Recursive range.
        LeetCode solution 1.
        """

        def is_valid_bst_helper(node, lower_limit, upper_limit):
            return (
                node is None or
                lower_limit < node.val < upper_limit and
                is_valid_bst_helper(node.left, lower_limit, node.val) and
                is_valid_bst_helper(node.right, node.val, upper_limit)
            )

        return is_valid_bst_helper(root, -float('inf'), float('inf'))

    def isValidBST0(self, root: TreeNode) -> bool:
        """
        Recursive range.
        LeetCode solution 1.
        """

        def is_valid_bst_helper(node, lower_limit, upper_limit):
            if node is None:
                return True

            if not (lower_limit < node.val < upper_limit):
                return False

            return (
                is_valid_bst_helper(node.left, lower_limit, node.val) and
                is_valid_bst_helper(node.right, node.val, upper_limit)
            )

        return is_valid_bst_helper(root, -float('inf'), float('inf'))
