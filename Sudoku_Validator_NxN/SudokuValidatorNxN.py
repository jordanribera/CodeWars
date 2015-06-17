import math

class Sudoku(object):

    def __init__(self, board):
        self.board = board
        
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def proper(self):
        n = len(self.board)
        
        for this_row in self.board:
            if len(this_row) != n:
                return False
                
        if (math.sqrt(n)).is_integer() != True:
            return False
            
        for this_row in self.board:
            for this_value in this_row:
                if this_value > n:
                    return False
                if this_value < 1:
                    return False
                if self.is_number(this_value) != True:
                    return False
                if this_value is True:
                    return False
            
        return True         
    
    def is_valid(self):
    
        print self.board
        print self.proper()
        if self.proper() != True:
            return False
        return self.validRows() and self.validColumns() and self.validBoxes()

    def validRows(self):
        n = len(self.board)
    
        for this_row in self.board:
            if len(set(this_row)) < n:
                return False
               
        return True
       
    def validColumns(self):
        n = len(self.board)
    
        columns = []
        for this_column in range(0,n):
            columns.append([])
    
        for this_row in self.board:
            for col_num in range (0,n):
                columns[col_num].append(this_row[col_num])
    
        for this_column in columns:
            if len(set(this_column)) < n:
                return False
               
        return True
       
    def validBoxes(self):
        n = len(self.board)
        box_dim = int(math.sqrt(n))
        
        boxes = []
        for this_box in range(0,n):
            boxes.append([])
    
        for row_num in range(0,n):
            for col_num in range(0,n):
                which_box = (row_num / box_dim) * box_dim + (col_num / box_dim)
                boxes[which_box].append(self.board[row_num][col_num])
    
        for this_box in boxes:
            if len(set(this_box)) < n:
                return False
               
        return True
