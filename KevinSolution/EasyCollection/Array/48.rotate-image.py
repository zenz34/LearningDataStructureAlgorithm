from collections import namedtuple
from typing import List

MatrixCell = namedtuple('MatrixCell', ['i', 'j'])

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rotate2(matrix)
        
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        LeetCode solution 1 - transpose, row reverse.
        """
        
        self.transpose(matrix)
        
        for row in matrix:
            row.reverse()
        
    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])        
        # transpose matrix
        for i in range(1, len(matrix)): # skip 0 since it's on diagonal
            for j in range(0, i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Iteratively rotate in cycles of outer square.
        """

        square_length = len(matrix[0])

        row_end = len(matrix)
        row_last = row_end - 1

        column_end = len(matrix[0])
        column_last = column_end - 1
        
        for i in range(square_length // 2):
            self.rotate_outer(
                matrix,
                # Start from 0, 0 (top-left) and move southeast by i, i.
                MatrixCell(i, i),
                # Start from `row_last`, `column_last` (bottom-right) and move northwest by i, i.
                MatrixCell(row_last - i, column_last - i)
            )

    def rotate0(self, matrix: List[List[int]]) -> None:
        """
        Recursively rotate in cycles of outer square.
        """

        row_end = len(matrix)
        row_last = row_end - 1

        column_end = len(matrix[0])
        column_last = column_end - 1

        self.rotate0_helper(
            matrix,
            MatrixCell(0, 0),
            MatrixCell(row_last, column_last)
        )

    def rotate0_helper(self, matrix: List[List[int]], start: MatrixCell, last: MatrixCell) -> None:
        width = last.i - start.i
        length = last.j - start.j
        if width <= 0 or length <= 0:
            return

        self.rotate_outer(matrix, start, last)

        # Done with rotating outer ring so recurse on inner square.
        self.rotate0_helper(
            matrix,
            # Move `start` southeast by 1, 1.
            MatrixCell(start.i + 1, start.j + 1),
            # Move `last` northwest by 1, 1.
            MatrixCell(last.i - 1, last.j - 1)
        )

    def rotate_outer(self, matrix: List[List[int]], start: MatrixCell, last: MatrixCell) -> None:
        row_start = start.j
        row_last = last.j
        row_end = row_last + 1

        square_length = row_end - row_start
        num_cycles = square_length - 1

        for i in range(num_cycles):
            top_left = MatrixCell(start.i, start.j + i)
            top_right = MatrixCell(start.i + i, last.j)
            bottom_right = MatrixCell(last.i, last.j - i)
            bottom_left = MatrixCell(last.i - i, start.j)

            # Keep swapping with `top_left` cell, so no need for temp variable.
            # `top_left` cell is the temp swap space.
            # Each square has 4 elements in a cycle to rotate, so need 3 swaps.
            # Each swap puts 1 element in the correct location, except the last swap,
            # which puts 2 elements in their correct locations.
            matrix[top_left.i][top_left.j], matrix[top_right.i][top_right.j] = (
                matrix[top_right.i][top_right.j], matrix[top_left.i][top_left.j]
            )
            matrix[top_left.i][top_left.j], matrix[bottom_right.i][bottom_right.j] = (
                matrix[bottom_right.i][bottom_right.j], matrix[top_left.i][top_left.j]
            )
            matrix[top_left.i][top_left.j], matrix[bottom_left.i][bottom_left.j] = (
                matrix[bottom_left.i][bottom_left.j], matrix[top_left.i][top_left.j]
            )
