import random


def draw_board(game_board, size):
    for row in game_board:
        print(row)
        print('')


def check_board(game_board, win, size):
    win = check_row(game_board, win, size)
    win = check_column(game_board, win, size)
    win = check_diagonal(game_board, win, size)
    return win


def check_row(game_board, win, size):
    for x in game_board:
        if x.count(1) == size:
            win = '1'
        if x.count(2) == size:
            win = '2'
    return win


def check_column(game_board, win, size):
    for s in range(0, size):
        column = []
        for m in game_board:
            column.append(m[s])
        if column.count(1) == size:
            win = '1'
        if column.count(2) == size:
            win = '2'
    return win


def check_diagonal(game_board, win, size):
    x = 0
    y = len(game_board[0])
    x_list = []
    y_list = []
    for m in game_board:
        x_list.append(m[x])
        x += 1
        y_list.append(m[y - 1])
        y -= 1
    if x_list.count(1) == size or y_list.count(1) == size:
        win = '1'
    if x_list.count(2) == size or y_list.count(2) == size:
        win = '2'
    return win


def count_zeros(game_board):
    count = 0
    for m in game_board:
        for i in range(0, len(m)):
            if m[i] == 0:
                count += 1
    return count


def player_turn(game_board, win, size, player=1):
    play = input(f'PLAYER {player} - Enter (row, col) to insert "{player}" token in the board EXAMPLE : 1,3 : ')
    player_crd = play.split(',')
    if game_board[int(player_crd[0]) - 1][int(player_crd[1]) - 1] != 0:
        play = input(f'Already Filled in Row & Col - Enter Different values - PLAYER {player} - Enter (row, col) to insert "{player}" token in the board EXAMPLE : 1,3 : ')
        player_crd = play.split(',')
    game_board[int(player_crd[0]) - 1][int(player_crd[1]) - 1] = player
    draw_board(game_board, board_size)
    print('-------------------------')
    return check_board(game_board, win, size)


def start_game(size):
    board = [[0 for _ in range(0, size)] for _ in range(0, size)]
    draw_board(board, size)
    winner = 'Draw'
    turn = 2
    while True:
        if count_zeros(board) == 0 and winner == 'Draw':
            print('The Match is Draw')
            break
        else:
            if winner != '2' and turn == 1:
                turn = 2
                winner = player_turn(board, winner, size, turn)
            elif winner != '1' and turn == 2:
                turn = 1
                winner = player_turn(board, winner, size, turn)
            if winner != 'Draw':
                print(f'Player " {winner} " won the match')
                break


print("WELCOME TO TIC-TOC-TOE GAME")
board_size = input("Enter game board size: ")
if not board_size.isdigit():
    print('Please enter number.....')
    board_size = input("Enter game board size: ")
else:
    board_size = int(board_size)
    if board_size == 0 and board_size > 5:
        print('Please enter value greater than zero and less than or equal to 5')
        board_size = input("Enter game board size: ")
start_game(board_size)

