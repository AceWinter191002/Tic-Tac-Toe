import random

print("""
 _____  _  _____       ______  ____   ______       _____  _____  ______         1 | 2 | 3 
/__ __\/ \/    __\    /__ __\/   _ \ /     _\     /__ __\/  _  \/   __/        ---+---+---  
  / \  | ||   / ______  / \  |  / \ ||    /  ______ / \  | / \ ||   \           4 | 5 | 6               | |  | ||   \_\______\| |  |  |-| ||    \_ \_____\| |  | \ / ||   /_         ---+---+---
  \_/  \_/ \____/       \_/  \_/  \_/ \____/        \_/  \_____/\______\        7 | 8 | 9                     Rules: Get 3 in a row, by choosing the open spots[1-9].
     """)

mode = ''
while not (mode == 'GOD MODE' or mode == 'EZ MODE'):
    print("Type your mode: God Mode/EZ Mode")
    mode = input().upper()

def drawBoard(board):
  
    print(board[1] + '  | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(board[4] + '  | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(board[7] + '  | ' + board[8] + ' | ' + board[9])

def inputPlayerLetter(): 
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[2] == letter and board[5] == letter and board[8] == letter) or # down the middle
    (board[3] == letter and board[6] == letter and board[9] == letter) or # down the right side
    (board[3] == letter and board[5] == letter and board[7] == letter) or # diagonal
    (board[1] == letter and board[5] == letter and board[9] == letter)) # diagonal

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Make your move: (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to {} Tic Tac Toe!'.format(mode))

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Victory! You have thwarted the machines' plans of world domination!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The machines have taken over... you have failed humanity...')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The computer requests a rematch!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break


