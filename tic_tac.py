from IPython.display import clear_output
def display_board(board):
    clear_outut()
    print(board[9]+'|'+board[8]+'|'+board[7])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3]) 
    

test_board = ['o','x','o','x','o','x','o','x']*10
display_board(test_board)

def player_input():
    maker = ''
    while not marker == 'x' or marker == 'o':
         marker = input("Player1: choose X or O:")  
    if marker == 'x':
        return('x','o')
    else:
        return('o','x')


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
   (board[1] == mark and board[2] == mark and board[3] == mark ) or
    (board[4] == board[5] == board[6]) 
