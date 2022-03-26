# write your code here
def checkRows(player, str):
    for i in range(0, 9, 3):
        win = True
        for j in range(0, 3):
            if str[i + j] != player:
                win = False
                break
        if win:
            return 0
    return 1

def checkDiag(player, str):

    if str[0] == str[4] == str[8] == player:
        return 0
    elif str[2] == str[4] == str[6] == player:
        return 0
    else:
        return 1

def checkCols(player, str):
    for i in range(0, 3):
        win = True
        for j in range(0, 3):
            if str[i + j * 3] != player:
                win = False
                break
        if win:
            return 0
    return 1

def possible(str):
    countX = 0
    countY = 0
    for i in str:
        if i == 'X':
            countX += 1
        if i == 'O':
            countY += 1
    if countX > countY + 1 or countY > countX + 1:
        return 0
    return 1

def draw(str):
    for i in range(0, 9):
        if str[i] == '_':
            return 0
    return 1

def winner(player, str):
    if not checkCols(player, str):
        return 0
    if not checkRows(player, str):
        return 0
    if not checkDiag(player, str):
        return 0
    return 1

def game(str):
    playerX = winner('X', str)
    playerO = winner('O', str)
    if not possible(str):
        print("Impossible")
    elif not (playerX or playerO):
        print("Impossible")
        return 0
    elif not playerX:
        print("X wins")
    elif not playerO:
        print("O wins")
    elif not draw(str):
        print("Game not finished")
    else:
        print("Draw")

def printBoard(string):
    for i in range(0, 9):
        if string[i] == '_':
            string[i] = ' '
    print('---------')
    print('|', string[0], string[1], string[2], '|')
    print('|', string[3], string[4], string[5], '|')
    print('|', string[6], string[7], string[8], '|')
    print('---------')

def move(str):
    check = True
    listed = []
    while check:
        listed = input("Enter the coordinates: ").split(' ')
        if not (listed[0].isnumeric() and listed[1].isnumeric()):
            print("You should enter numbers!")
            continue
        if int(listed[0]) > 3 or int(listed[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        local = (int(listed[0]) - 1) * 3 + (int(listed[1]) - 1)
        print(local, str)
        if str[local] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            str[local] = 'X'
            check = False

string = input()
string = list(string)
printBoard(string)
move(string)
printBoard(string)
