def result(cell):
    win = ''
    flag_x = 0
    flag_o = 0
    # rows
    row_ctr = 0
    ch = ' '
    for i in range(3):
        ch = cell[i][0]
        row_ctr = 0
        for j in range(3):
            if cell[i][j] == ch:
                row_ctr += 1
        if row_ctr == 3:
            if ch == 'X':
                flag_x = 1
            elif ch == 'O':
                flag_o = 1
            break

    # columns:
    if row_ctr != 3:
        ch_col = ' '
        for i in range(3):
            ch_col = cell[0][i]
            col_ctr = 0
            for j in range(3):
                if cell[j][i] == ch_col:
                    row_ctr += 1
            if col_ctr == 3:
                if ch_col == 'X':
                    flag_x = 1
                elif ch_col == 'O':
                    flag_o = 1
                break

    # diagonals:
    if cell[0][0] == cell[1][1] == cell[2][2] or cell[0][2] == cell[1][1] == cell[2][0]:
        if cell[1][1] == 'X':
            flag_x = 1
        elif cell[1][1] == 'O':
            flag_o = 1

    global mov_ctr
    if flag_o == 1:
        win = 'O wins'
    elif flag_x == 1:
        win = 'X wins'
    if flag_x == 0 and flag_o == 0 and mov_ctr == 9:
        win = 'Draw'
    return win


def printing(cell):
    print(" ---------")
    print(" | {} {} {} |".format(cell[0][0], cell[0][1], cell[0][2]))
    print(" | {} {} {} |".format(cell[1][0], cell[1][1], cell[1][2]))
    print(" | {} {} {} |".format(cell[2][0], cell[2][1], cell[2][2]))
    print(" ---------")


lis = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
playing = True
mov_ctr = 0
res = ''
ticket = ''
x, y = 0, 0
while playing:
    printing(lis)
    d = 0
    x, y = 0, 0

    while d == 0:
        x, y = input("Enter the coordinates: ").split()
        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
        elif int(x) not in range(1, 4) or int(y) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
        elif lis[3 - int(y)][int(x) - 1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            d = 1

    if mov_ctr % 2 == 0:
        ticket = 'X'
    else:
        ticket = 'O'

    lis[3 - int(y)][int(x) - 1] = ticket
    mov_ctr += 1
    if mov_ctr > 4:
        res = result(lis)
        if res == 'X wins' or res == 'O wins' or res == 'Draw' or mov_ctr == 9:
            playing = False

lis[3 - int(y)][int(x) - 1] = ticket
printing(lis)
print(res)
