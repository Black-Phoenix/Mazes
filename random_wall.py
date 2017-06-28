import random

random.seed(None)
max_len = 20
size = [max_len, max_len]
maze_whole = []
for i in range(size[0]):
    temp = []
    for j in range(size[1]):
        temp.append(0)
    maze_whole.append(temp)


def walls(maze, size):
    wall = [random.randint(size[0][0] + 1, size[1][0] - 1), random.randint(size[0][1] + 1, size[1][1] - 1)]
    print wall
    for i in range(size[0][0], size[1][0]+1):
        maze[i][wall[1]] += 1
    for i in range(size[0][1], size[1][1]+1):
        maze[wall[0]][i] += 2
    return wall


def holes(maze, size, wall):
    double_holes = random.randint(0, 1)
    hole = []
    if double_holes == 0:
        hole.append([wall[0], random.randint(size[0][1], wall[1] - 1)])
        hole.append([wall[0], random.randint(wall[1] + 1, size[1][1])])
        last_hole = wall[0]
        while last_hole == wall[0]:
            last_hole = random.randint(size[0][0], size[1][0])
        hole.append([last_hole, wall[1]])
    else:
        hole.append([random.randint(size[0][0], wall[0] - 1), wall[1]])
        hole.append([random.randint(wall[0] + 1, size[1][0]), wall[1]])
        last_hole = wall[1]
        while last_hole == wall[1]:
            last_hole = random.randint(size[0][1], size[1][1])
        hole.append([wall[0], last_hole])
    print hole
    for i in hole:
        maze[i[0]][i[1]] = 0


def print_maze(maze):
    for pos_i, i in enumerate(maze):
        for pos_j, j in enumerate(i):
            if pos_i==0 or pos_j == 0 or pos_i==max_len-1 or pos_j == max_len-1:
                print "*",
            elif j == 3:
                print "+",
            elif j == 1:
                print "|",
            elif j == 2:
                print "-",
            elif j == 0:
                print " ",
            else:
                print "!",
        print ""

queue = [[[0, 0], [max_len-1, max_len-1]]]
while len(queue) != 0:
    temp = queue[0]
    print temp
    del queue[0]
    if ((temp[1][0] - temp[0][0]-1)*(temp[1][1]-temp[0][1]-1)) <= 2:
        print "Too small"
        continue
    wall = walls(maze_whole, temp)

    #print_maze(maze_whole)
    holes(maze_whole, temp, wall)
    #RT
    queue.append([[temp[0][0], wall[1]+1], [wall[0]-1, temp[1][1]]])
    #LB
    queue.append([[wall[0]+1,temp[0][1]], [temp[1][0], wall[1]-1]])
    #LT
    queue.append([[temp[0][0], temp[0][1]], [wall[0]-1, wall[1]-1]])
    #RB
    queue.append([[wall[0]+1, wall[1]+1], [temp[1][0], temp[1][1]]])

print_maze(maze_whole)
