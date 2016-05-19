def validSolution(board):
    return validRows(board) and validColumns(board) and validBoxes(board)


def validRows(board):
    for this_row in board:
        if len(set(this_row)) < 9:
            return False

    return True


def validColumns(board):

    columns = [[], [], [], [], [], [], [], [], []]

    for this_row in board:
        for col_num in range(0, 9):
            columns[col_num].append(this_row[col_num])

    for this_column in columns:
        if len(set(this_column)) < 9:
            return False

    return True


def validBoxes(board):
    boxes = [[], [], [], [], [], [], [], [], []]

    for row_num in range(0, 9):
        for col_num in range(0, 9):
            which_box = (row_num / 3) * 3 + (col_num / 3)
            boxes[which_box].append(board[row_num][col_num])

    for this_box in boxes:
        if len(set(this_box)) < 9:
            return False

    return True
