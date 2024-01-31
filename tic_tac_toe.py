# our data stored in a dictionary
board = {
    'top-l':' ', 'top-m':' ', 'top-r':' ',
    'mid-l':' ', 'mid-m':' ', 'mid-r':' ',
    'low-l':' ', 'low-m':' ', 'low-r':' '
}


##### display board method
def displayGame():
    print()
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-' + '+' + '-' + '+' + '-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-' + '+' + '-' + '+' + '-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
#####

#####
def startGame():
    x_turn = True

    i = 1
    while i <= 9:
        # display the board in every cycle
        displayGame()

        # check if we have a winner
        if board['top-l'] == board['top-m'] == board['top-r'] and board['top-l'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['mid-l'] == board['mid-m'] == board['mid-r'] and board['mid-l'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['low-l'] == board['low-m'] == board['low-r'] and board['low-l'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['top-l'] == board['mid-l'] == board['low-l'] and board['top-l'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['top-m'] == board['mid-m'] == board['low-m'] and board['top-m'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['top-r'] == board['mid-r'] == board['low-r'] and board['top-r'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['top-l'] == board['mid-m'] == board['low-r'] and board['top-l'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0
        elif board['top-r'] == board['mid-m'] == board['low-l'] and board['top-r'] != ' ':
            print('O' if x_turn else 'X', 'WINS')
            return 0

        print('X' if x_turn else 'O', 'Turn:', end=' ')
        
        # get input & check if it is correct
        res = input()
        if res not in board.keys() or board[res] != ' ':
            print('*'*11 + '\nWRONG INPUT, ENTER: \'top-l\' \'top-m\' \'top-r\' \'mid-l\' \'mid-m\' \'mid-r\' \'low-l\' \'low-m\' \'low-r\'\n' + '*'*11)
            continue

        board[res] = 'X' if x_turn else 'O'
        x_turn = (False if x_turn else True)

        i += 1
    
    # it is a draw
    print('DRAW')
    return 0
#####
        
# start the game
startGame()