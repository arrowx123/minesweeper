import sys
import math
import queue
import random
"""
Hyperparameter
"""
percent_of_mine = 0.3
"""
Get the size of the board.
"""
while True:
    num_of_row = input('num_of_row: ')
    try:
        num_of_row = int(num_of_row)
        break
    except:
        pass

while True:
    num_of_col = input('num_of_col: ')
    try:
        num_of_col = int(num_of_col)
        break
    except:
        pass

board = [['' for i in range(num_of_col)] for j in range(num_of_row)]


def print_board():
    print()
    for rows in board:
        string = ''
        for col in rows:
            if col == '':
                string += 'X'
            elif col == ' ':
                string += 'O'
            else:
                string += str(col)
        print(string)


"""
Generate mines
"""

num_of_mine = math.ceil(percent_of_mine * num_of_row * num_of_col)
num_of_not_mine = num_of_row * num_of_col - num_of_mine
mine = set()

while True:
    x = random.randint(0, num_of_row - 1)
    y = random.randint(0, num_of_col - 1)

    mine.add((x, y))
    if len(mine) == num_of_mine:
        break

for ele in mine:
    print(ele)

status = 0


def check_status():
    if status == -1:
        print("Lose.")
        sys.exit()
    elif status == 1:
        print("Win.")
        sys.exit()


def valid_pos(x, y):
    if x >= 0 and x < num_of_row and y >= 0 and y < num_of_col:
        return True
    return False


def get_nearby(x, y):
    x_diffs = [-1, 0, 0, 1]
    y_diffs = [0, -1, 1, 0]

    nearby_mine = []
    nearby_no_mine = []
    for x_diff, y_diff in zip(x_diffs, y_diffs):
        c_x = x + x_diff
        c_y = y + y_diff

        if valid_pos(c_x, c_y):
            if (c_x, c_y) in mine:
                nearby_mine.append((c_x, c_y))
            else:
                nearby_no_mine.append((c_x, c_y))
    return nearby_mine, nearby_no_mine


"""
User play
    1) get position

    2) If mine:
           game over
       If not mine:
           if nearby mine:
               display number
           if not nearby mine:
               recursively display nearby position

    3) If display enough:
           Win
"""

visited = set()

while True:
    """
    read input
    """
    print_board()
    while True:
        while True:
            x = input('x: ')
            try:
                x = int(x)
                if x >= 0 and x < num_of_row:
                    break
            except:
                pass

        while True:
            y = input('y: ')
            try:
                y = int(y)
                if y >= 0 and y < num_of_col:
                    break
            except:
                pass
        if (x, y) in visited:
            print("already visited.")
        else:
            break
    """
    process input
    """
    positions = queue.Queue()
    positions.put((x, y))

    while True:
        if positions.qsize() == 0:
            break
        c_x, c_y = positions.get()
        visited.add((c_x, c_y))

        if (c_x, c_y) in mine:
            status = -1
            print("({}, {}) is a mine.".format(c_x, c_y))
            break

        nearby_mine, nearby_no_mine = get_nearby(c_x, c_y)
        print(nearby_mine)
        print(nearby_no_mine)
        if len(nearby_mine) != 0:
            num_of_nearby_mine = len(nearby_mine)
            board[c_x][c_y] = str(num_of_nearby_mine)
        else:
            board[c_x][c_y] = ' '
            for ele in nearby_no_mine:
                x, y = ele
                if (x, y) not in visited:
                    positions.put((x, y))
    print(visited)
    if len(visited) == num_of_not_mine:
        status = 1

    check_status()
