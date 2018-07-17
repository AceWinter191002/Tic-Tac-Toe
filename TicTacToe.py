import random

print("""
 _____  _  _____       ______  ____   ______       _____  _____  ______         1 | 2 | 3
/__ __\/ \/    __\    /__ __\/   _ \ /     _\     /__ __\/  _  \/   __/        ---+---+---
  / \  | ||   / ______  / \  |  / \ ||    /  ______ / \  | / \ ||   \           4 | 5 | 6               | |  | ||   \_\______\| |  |  |-| ||    \_ \_____\| |  | \ / ||   /_         ---+---+---
  \_/  \_/ \____/       \_/  \_/  \_/ \____/        \_/  \_____/\______\        7 | 8 | 9                Rules: Defeat your enemy by getting 3 in a row, by choosing the open spots[1-9].
     """)


def drawBoard(board):  
    print(board[1] + '  | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(board[4] + '  | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(board[7] + '  | ' + board[8] + ' | ' + board[9])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('PLAYER ONE: Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[1] == bo[2] == bo[3] == le) or # across the top
    (bo[4] == bo[5] == bo[6] == le) or # across the middle
    (bo[7] == bo[8] == bo[9] == le) or # across the bottom
    (bo[1] == bo[4] == bo[7] == le) or # down the left side
    (bo[2] == bo[5] == bo[8] == le) or # down the middle
    (bo[3] == bo[6] == bo[9] == le) or # down the right side
    (bo[3] == bo[5] == bo[7] == le) or # diagonal
    (bo[9] == bo[5] == bo[1] == le)) # diagonal

def getBoardCopy(board):
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
        print('{}: What is your next move? (1-9)'.format(turn))
        move = input()
    return int(move)

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to PVP Tic Tac Toe!')

counter = 1
while counter<10:
    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying and counter<10:
        if turn == 'Player 1':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            counter = counter + 1

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! Player 1 has achieved victory!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    
                else:
                    turn = 'Player 2'
        else:
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player2Letter, move)
            counter = counter + 1

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('Awesome! Player 2 reigns superior!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    
                else:
                    turn = 'Player 1'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        exit()
