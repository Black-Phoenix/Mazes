import random

random.seed(None)
max_len = 20
size = [max_len, max_len]
maze_whole = []

#fill with walls
for i in range(size[0]):
    temp = []
    for j in range(size[1]):
        temp.append(0)
    maze_whole.append(temp)

def degree_of_freedom(pos):
    return maze_whole[pos[0]+1][pos[1]]+maze_whole[pos[0]-1][pos[1]]+maze_whole[pos[0]][pos[1]+1]+maze_whole[pos[0]][pos[1]-1]

def DFS(pos):
    set_of_moves = []
    maze_whole[pos[0]][pos[1]] = 1
    if pos[0] < max_len - 2 and maze_whole[pos[0]+1][pos[1]] == 0:
        set_of_moves.append([pos[0]+1, pos[1]])
    if pos[0] > 1 and maze_whole[pos[0]-1][pos[1]] == 0:
        set_of_moves.append([pos[0]-1, pos[1]])
    if pos[1] < max_len - 2 and maze_whole[pos[0]][pos[1]+1] == 0:
        set_of_moves.append([pos[0], pos[1]+1])
    if pos[1] > 1 and maze_whole[pos[0]][pos[1]-1] == 0:
        set_of_moves.append([pos[0], pos[1]-1])
    while len(set_of_moves) != 0:
        x = random.randint(0, len(set_of_moves)-1)
        if degree_of_freedom(set_of_moves[x]) == 1:
            DFS(set_of_moves[x])
        del set_of_moves[x]

def print_maze(maze):
    for pos_i, i in enumerate(maze):
        for pos_j, j in enumerate(i):
            if j == 3:
                print " ",
            elif j == 1:
                print " ",
            elif j == 2:
                print " ",
            elif j == 0:
                print "*",
            else:
                print " ",
        print ""
    print ""

DFS([1,1])
print_maze(maze_whole)