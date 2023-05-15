# in this case
# bot choice number at random

from random import choice


board = [ 0,
         ' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
board_for_bot = [1,2,3,4,5,6,7,8,9] # bot can check which number is left through this

player = 'X'
bot = 'O'
turn = True # true -> player is first, false -> bot is first


# draw board
def print_board():
    print(' ' + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------")
    print(' ' + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(' ' + board[1] + " | " + board[2] + " | " + board[3])
    print("\n")


# check finish
def check_finish():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    elif len(board_for_bot) == 0:
        return True
    else:
        return False


# is it playing?
playing = True


# main process
while playing:
    print_board()

    if turn:
        while True:
            a = int(input())

            if a in board_for_bot:
                del board_for_bot[board_for_bot.index(a)]
                board[a] = 'X'
                break

        turn = False
    else:
        a = choice(board_for_bot)
        del board_for_bot[board_for_bot.index(a)]
        board[a] = 'O'
        turn = True

    if check_finish():
        playing = False


print_board()
