# TicTacToe game
def display_board(board):
    print(' | |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(' | |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(' | |')
    print(board[1]+'|'+board[2]+'|'+board[3])
# accepting user input X or O
def user_input():
    marker = ''
    while marker != 'X' and marker  != 'O':
        marker = input('Player1 please choose X or O:').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
##board,marker,positon
def place_marker(board,marker,positon):
    board[positon] = marker
# win check
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #horizontal
            (board[4] == mark and board[5] == mark and board[6] == mark) or #horizontal
            (board[1] == mark and board[2] == mark and board[3] == mark) or #horizontal
            (board[1] == mark and board[4] == mark and board[7] == mark) or #vertical
            (board[2] == mark and board[5] == mark and board[8] == mark) or #vertical
            (board[3] == mark and board[6] == mark and board[9] == mark) or #vertial
            (board[1] == mark and board[5] == mark and board[9] == mark) or #dioagnal
            (board[3] == mark and board[5] == mark and board[7] == mark)) 
#random
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'player 1'
#check for free space on board
def space_check(board,positon):
    return board[positon] == ' '
#return boolean after checking
def full_space_check(board):
    for i in range(1,10):
        if space_check(board , i):
            return False
    return True
#player choice 
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position
#replay game
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
## combining functions and running game
print('welcome to Tic Tac Toe')
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = user_input()
    turn = choose_first()
    print(turn + 'Will go first.')
    play_game = input('Ready to play?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_space_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:#player 2
            if turn == 'Player 2':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_space_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
    


             
        





                