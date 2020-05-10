class Solution:
    SUB_BOXES_PER_ROW = SUB_BOXES_PER_COLUMN = 3
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidSudoku0(board)
        
    def isValidSudoku0(self, board: List[List[str]]) -> bool:
        """
        Maintain 3 sets, row, column, sub-box - one for each validation of a cell.
        When inserting a cell into a set, also insert the cell so the set can check
        for duplicates.
        """
        
        row_set = set()
        column_set = set()
        sub_box_set = set()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != '.': # can use `continue` but slows down runtime for some reason
                    row_pair = (i, cell)
                    column_pair = (j, cell)
                    sub_box_index = (
                        i // type(self).SUB_BOXES_PER_ROW,
                        j // type(self).SUB_BOXES_PER_COLUMN
                    )
                    sub_box_pair = (sub_box_index, cell)
                    if (
                        row_pair in row_set or
                        column_pair in column_set or
                        sub_box_pair in sub_box_set
                    ):
                        return False
                    row_set.add(row_pair)
                    column_set.add(column_pair)
                    sub_box_set.add(sub_box_pair)
        return True
