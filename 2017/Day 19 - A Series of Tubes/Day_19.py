import numpy as np

#                      Moving functions:
# ------------------------------------------------------------------
def move_right(x, y):
    return x, y-1

def move_down(x, y):
    return x-1, y

def move_left(x, y):
    return x, y+1

def move_up(x, y):
    return x+1, y

def move(dir,pos):
    global alphabet
    global maze
    global left, right, up, down

    letters_found = 0
    ordered_letters = []

    x = pos[0]
    y = pos[1]

    while letters_found < 9:
        if dir == down:
            x, y = move_down(x, y)
        elif dir == up:
            x, y = move_up(x, y)
        elif dir == left:
            x, y = move_left(x, y)
        elif dir == right:
            x, y = move_right(x, y)
        if maze[x,y] == "+":
            if dir == up or dir == down:
                if maze[x-1, y] == "-":
                    dir = right
                else:
                    dir = left
            else:
                if maze[x, y-1] == "|":
                    dir = down
                else:
                    dir = up

        elif maze[x,y] in alphabet:
            ordered_letters.append(maze[x,y])
            letters_found += 1

    text = ""
    for i in ordered_letters:
        text += i

    return text

#                      Build the maze:
# ------------------------------------------------------------------
file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = [line.rstrip() for line in file.readlines()]
np.set_printoptions(suppress=True, linewidth=200)

x_range = len(lines)
y_range = max([len(l) for l in lines ])

maze = np.array(range(x_range*y_range), dtype=str).reshape(x_range,y_range)

for x in range(x_range):
    for y in range(y_range):
        try:
            maze[x, y] = str(lines[x][y])
        except IndexError:
            maze[x, y] = " "

'''
#                  Print the maze to check:
# ------------------------------------------------------------------

maze_txt = []
for x in range(x_range):
    maze_line = ""
    for y in range(y_range):
        maze_line += maze[x, y]
    maze_txt.append(maze_line)

for line in maze_txt:
    print(line)
'''

#                    Initialise variables:
# -----------------------------------------------------------------

up = 'up'
down = 'down'
left = 'left'
right = 'right'

current_pos = [0, 0]
cur_dir = down
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters = []

#              Find start pos and amount of letters
# -----------------------------------------------------------------

for y in range(y_range):
    if maze[0, y] == "|":
        current_pos = [1, y]
    for x in range(x_range):
        if maze[x, y] in alphabet:
            letters.append(maze[x,y])

print(move(cur_dir, current_pos))
