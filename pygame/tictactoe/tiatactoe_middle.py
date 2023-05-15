# in this case
# bot choice number with algoritm
# optimize X
# it can see 3 steps of future

from copy import deepcopy
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
def check_finish(board_1):
    if (board_1[1] == board_1[2] and board_1[1] == board_1[3] and board_1[1] != ' '):
        return True
    elif (board_1[4] == board_1[5] and board_1[4] == board_1[6] and board_1[4] != ' '):
        return True
    elif (board_1[7] == board_1[8] and board_1[7] == board_1[9] and board_1[7] != ' '):
        return True
    elif (board_1[1] == board_1[4] and board_1[1] == board_1[7] and board_1[1] != ' '):
        return True
    elif (board_1[2] == board_1[5] and board_1[2] == board_1[8] and board_1[2] != ' '):
        return True
    elif (board_1[3] == board_1[6] and board_1[3] == board_1[9] and board_1[3] != ' '):
        return True
    elif (board_1[1] == board_1[5] and board_1[1] == board_1[9] and board_1[1] != ' '):
        return True
    elif (board_1[7] == board_1[5] and board_1[7] == board_1[3] and board_1[7] != ' '):
        return True
    elif len(board_for_bot) == 0:
        return True
    else:
        return False


def which_one_is_best():
    score = [0, ]
    for i in range(1, 10):
        if i in board_for_bot:
            score.append(100)
        else:
            score.append(0)

    for i in board_for_bot:
        present_board = deepcopy(board)
        present_board_for_bot = deepcopy(board_for_bot)

        present_board[i] = 'O'
        del present_board_for_bot[present_board_for_bot.index(i)]

        if check_finish(present_board):
            score[i] += 1
        else:
            for j in present_board_for_bot:
                present_board[j] = 'X'

                if check_finish(present_board):
                    score[i] -= 1

                present_board[j] = ' '

    a = max(score)
    max_index = []

    for i in range(1, 10):
        if score[i] == a:
            max_index.append(i)

    return choice(max_index)


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
        a = which_one_is_best()
        del board_for_bot[board_for_bot.index(a)]
        board[a] = 'O'
        turn = True

    if check_finish(board):
        playing = False


print_board()
