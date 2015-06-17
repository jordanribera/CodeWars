def sudoku(puzzle):
    solved = False
    while solved is not True:
        solved = True
        possibilities = getPossibilities(puzzle)
        for rowNum in range (0,9):
            for colNum in range (0,9):
                if puzzle[rowNum][colNum] == 0:
                    solved = False
                    if len(possibilities[rowNum][colNum]) == 1:
                        puzzle[rowNum][colNum] = possibilities[rowNum][colNum][0]

    return puzzle
    
def getPossibilities(puzzle):
    columns = [[],[],[],[],[],[],[],[],[]]
    for rowNum in range (0,9):
        for colNum in range (0,9):
            columns[colNum].append(puzzle[rowNum][colNum])
    
    boxes = [[],[],[],[],[],[],[],[],[]]
    for rowNum in range (0,9):
        for colNum in range (0,9):
            whichBox = (rowNum / 3) * 3 + (colNum / 3)
            boxes[whichBox].append(puzzle[rowNum][colNum])
            
    possibilities = [[],[],[],[],[],[],[],[],[]]
    for rowNum in range (0,9):
        for colNum in range (0,9):
            possibilities[rowNum].append([1,2,3,4,5,6,7,8,9])
            for thisRowInstance in set(puzzle[rowNum]):
                if thisRowInstance in possibilities[rowNum][colNum]:
                    possibilities[rowNum][colNum].remove(thisRowInstance)
            for thisColumnInstance in set(columns[colNum]):
                if thisColumnInstance in possibilities[rowNum][colNum]:
                    possibilities[rowNum][colNum].remove(thisColumnInstance)
            boxNum = (rowNum / 3) * 3 + (colNum / 3)
            for thisBoxInstance in set(boxes[boxNum]):
                if thisBoxInstance in possibilities[rowNum][colNum]:
                    possibilities[rowNum][colNum].remove(thisBoxInstance)
                
    return possibilities
