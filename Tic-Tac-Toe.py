
# Making tic tac toe game using python

board = ['-','-','-',
         '-','-','-',
         '-','-','-']
currentPlayer = 'X'
winner = None
gameRunning = True

# Printing the board
def printBoard(board):
    print(board[0], ' | ', board[1], ' | ', board[2])
    print('--------------')
    print(board[3], ' | ', board[4], ' | ', board[5])
    print('--------------')
    print(board[6], ' | ', board[7], ' | ', board[8])

# Taking the player input
def playerInput(board):
    inp = int(input('Enter number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Oops')

# Check Horizontally
def checkHori(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != '-':       
        winner = board[6]
        return True

# Check Vertically
def checkVer(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != '-':       
        winner = board[1]
        return True
    
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

# Check Diagonal    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

# Check tie
def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print('Its a Tie')
        gameRunning = False

# Check win
def checkWin(board):
    if checkHori(board) or checkVer(board) or checkDiag(board):     
        print(f'The winner is {winner}')


# Switch player
def switchPlayer(board):
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


# Game running
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkHori(board)
    checkVer(board)
    checkDiag(board)
    checkTie(board)
    checkWin(board)
    switchPlayer(board)

 
