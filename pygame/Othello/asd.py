delta = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

def game(k):
    board = [
            [7,  7,  7,  7,  7,  7,  7,  7,  7, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1,  0,  1, -1, -1, -1, 7],
            [7, -1, -1, -1,  1,  0, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7,  7,  7,  7,  7,  7,  7,  7,  7, 7]
    ]

    put = [list(map(int, input().split())) for i in range(k)]
    turn = True # 흑이면 트루, 백이면 뻘스
    for i in put:
        for direction in delta:
            x, y = i
            dx, dy = direction
            board[x][y] = int(turn)
            change_list = []

            while True:
                x += dx
                y += dy
                if board[x][y] == int(turn):
                    break
                if board[x][y] == 7 or board[x][y] == -1:
                    change_list = []
                    break
                if board[x][y] != int(turn):
                    change_list.append([x, y])

            if change_list:
                for j in change_list:
                    board[j[0]][j[1]] = int(turn)

        turn = not turn

    return board


def count(board):
    black = 0
    white = 0
    for i in board[1:-1]:
        black += i.count(1)
        white += i.count(0)

    return black, white

for i in range(int(input())):
    k = int(input())
    board = game(k)

    print(*count(board))
    for i in board[1:-1]:
        for j in i[1:-1]:
            if j == 0:
                print('O', end='')
            elif j == 1:
                print('X', end='')
            else:
                print('+', end='')
        print()
