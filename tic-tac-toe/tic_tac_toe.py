board = ['_',]*9
# print(board)


def drawBoard(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('_'*9)
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('_'*9)
    print(board[6]+' | '+board[7]+' | '+board[8])


gameRunning = True
currentPlayer = 'X'


def getUserInput(board):
    imp = int(input('Enter the num from 1-9: '))
    print(imp)
    if imp >= 1 and imp <= 9 and board[imp-1] == '_':
        board[imp-1] = currentPlayer
    else:
        print('Invalid Move!')


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'


def checkWinOrTie(board):
    global currentPlayer
    global gameRunning
    # check row

    def checkRow(board):
        if board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
        elif board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
        elif board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
    # check Column

    def checkColumn(board):
        if board[0] == currentPlayer and board[3] == currentPlayer and board[6] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
        elif board[1] == currentPlayer and board[4] == currentPlayer and board[7] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
        elif board[2] == currentPlayer and board[5] == currentPlayer and board[8] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True

    # check diagnoal
    def checkDiag(board):
        if board[0] == currentPlayer and board[4] == currentPlayer and board[8] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True
        elif board[2] == currentPlayer and board[4] == currentPlayer and board[6] == currentPlayer:
            print(f"Winner is {currentPlayer}")
            return True

    def checkTie(board):
        if '_' not in board:
            print('TIE')
            return True

    if checkRow(board) or checkColumn(board) or checkDiag(board) or checkTie(board):
        gameRunning = False


while gameRunning:

    drawBoard(board)
    getUserInput(board)
    drawBoard(board)
    checkWinOrTie(board)
    switchPlayer()
    print('\n'*3)
