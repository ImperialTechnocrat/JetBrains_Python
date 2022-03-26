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

string = input()
print('---------')
print('|', string[0], string[1], string[2], '|')
print('|', string[3], string[4], string[5], '|')
print('|', string[6], string[7], string[8], '|')
print('---------')
game(string)
