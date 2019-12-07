# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn/solutions  #
def check_row(grid):
    for i in range(len(grid)):
        elements = set()
        for i in grid[i]:
            if i != '.':
                if i in elements:
                    return False
                else:
                    elements.add(i)

    return True



def check_column(grid):
    for i in range(len(grid)):
        elements = set()
        for j in range(len(grid)):
            e = grid[j][i]
            if e != '.':
                if e in elements:
                    return False
                else:
                    elements.add(e)
    return True
					

def check_subsquare(grid):
    row, column = 0, 0
    while row <= 6 and column <= 6:
        # print(f'iteration : {row} {column}')
        elements = set()
        for i in range(row, row + 3):
            for j in range(column, column + 3):
                e = grid[i][j]
                print(i, j, e)
                if e != '.':
                    if e in elements:
                        # print('Here: Returning False')
                        return False
                    else:
                        elements.add(e)

        if column < 6:
            column += 3
        else:
            column = 0
            row += 3


    return True


def sudoku2(grid):
    row_check = check_row(grid)
    if not row_check:
        return False

    print('Row_clear')
    column_check = check_column(grid)
    if not column_check:
        return False
    
    print('column_clear')
    subsquare_check = check_subsquare(grid)
    if not subsquare_check:
        return False
    return True
