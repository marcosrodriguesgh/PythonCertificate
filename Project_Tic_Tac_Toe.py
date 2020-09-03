from random import randint

def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    count = 0
    for linha in board:
        print(f'+-------' * 3 + '+')
        print(f'|       ' * 3 + '|')
        for col in linha:
            print(f'|   {col}   ', end='')
        print('|')
        print(f'|       ' * 3 + '|')
    print(f'+-------' * 3 + '+')

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    while True:
        mov = int(input('Enter your move: '))
        opcaoValida = False
        for item in MakeListOfFreeFields(board):
            if str(mov) == item[2]:
                row = int(item[0])
                col = int(item[1])
                opcaoValida = True
        if opcaoValida:
            break
        else:
            print('Invalid move!')
    board[row][col] = 'O'
    DisplayBoard(board)
    return board

def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    freeFields = []
    for linha, tripla in enumerate(board):
        for coluna, item in enumerate(tripla):
            if str(item) not in 'XxOo':
                freeFields.append(str(linha)+str(coluna)+str(item))
    return freeFields

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] or board[0][r] == board[1][r] == board[2][r] \
                or board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            alguemVenceu = True
        else:
            alguemVenceu = False
    if alguemVenceu and sign == 'O':
        print('Você venceu, parabens!')
        return True
    elif alguemVenceu and sign == 'X':
        print('Você perdeu, o computador venceu! Tente novamente!')
        return True
    return False

def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    freeFields = MakeListOfFreeFields(board)
    comp = randint(0, len(freeFields)-1)
    board[int(freeFields[comp][0])][int(freeFields[comp][1])] = 'X'
    DisplayBoard(board)
    return board


board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
DisplayBoard(board)
while len(MakeListOfFreeFields(board)) > 0:
    board = EnterMove(board)
    if VictoryFor(board, 'O'):
        break
    board = DrawMove(board)
    if VictoryFor(board, 'X'):
        break
else:
    print('Houve um empate, tente novamente.')