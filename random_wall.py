import random


# Create the 2 walls
def walls(maze, size):
    wall = [random.randint(size[0][0] + 1, size[1][0] - 1), random.randint(size[0][1] + 1, size[1][1] - 1)]
    print wall
    for i in range(size[0][0], size[1][0]+1):
        maze[i][wall[1]] += 1
    for i in range(size[0][1], size[1][1]+1):
        maze[wall[0]][i] += 2
    return wall


# create 3 holes in the walls
def holes(maze, curr_size, curr_wall):
    double_holes = random.randint(0, 1)
    hole = []
    if double_holes == 0:
        hole.append([curr_wall[0], random.randint(curr_size[0][1], curr_wall[1] - 1)])
        hole.append([curr_wall[0], random.randint(curr_wall[1] + 1, curr_size[1][1])])
        last_hole = curr_wall[0]
        while last_hole == curr_wall[0]:
            last_hole = random.randint(curr_size[0][0], curr_size[1][0])
        hole.append([last_hole, curr_wall[1]])
    else:
        hole.append([random.randint(curr_size[0][0], curr_wall[0] - 1), curr_wall[1]])
        hole.append([random.randint(curr_wall[0] + 1, curr_size[1][0]), curr_wall[1]])
        last_hole = curr_wall[1]
        while last_hole == curr_wall[1]:
            last_hole = random.randint(curr_size[0][1], curr_size[1][1])
        hole.append([curr_wall[0], last_hole])
    print hole
    for i in hole:
        maze[i[0]][i[1]] = 0


# Display the maze in a human viewable format.
# 1 -> Vertical wall
# 2 -> Horizontal wall
# 3 -> Intersection
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

if __name__ == '__main__':
    random.seed(None)
    max_len = 20
    size = [max_len, max_len]
    maze_whole = []
    for i in range(size[0]):
        temp = []
        for j in range(size[1]):
            temp.append(0)
        maze_whole.append(temp)
    queue = [[[0, 0], [max_len-1, max_len-1]]]
    while len(queue) != 0:
        temp = queue[0]
        print temp
        del queue[0]
        if ((temp[1][0] - temp[0][0]-1)*(temp[1][1]-temp[0][1]-1)) <= 2:
            print "Too small to divide with 2 walls"
            continue
        wall = walls(maze_whole, temp)
        holes(maze_whole, temp, wall)
        # Adding the 4 new quadrants to the queue to process
        #RT
        queue.append([[temp[0][0], wall[1]+1], [wall[0]-1, temp[1][1]]])
        #LB
        queue.append([[wall[0]+1, temp[0][1]], [temp[1][0], wall[1]-1]])
        #LT
        queue.append([[temp[0][0], temp[0][1]], [wall[0]-1, wall[1]-1]])
        #RB
        queue.append([[wall[0]+1, wall[1]+1], [temp[1][0], temp[1][1]]])

    print_maze(maze_whole)
