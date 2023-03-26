import random

# ----------- creating a random maze ----------------
height = 6
width = 6

maze = []
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(0)
    maze.append(line)

start_column = random.randint(0,1)
start_row = random.randint(0,5)

end_column = random.randint(4,5)
end_row = random.randint(0,5)

maze[start_row][start_column] = 5
maze[end_row][end_column] = 8

count = 0
while (count < 4):
    barrier_column = random.randint(0,5)
    barrier_row = random.randint(0,5)
    if (barrier_column == start_column and barrier_row == start_row) or (barrier_column == end_column and barrier_row == end_row):
        count = count
        continue
    maze[barrier_row][barrier_column] = 1
    count += 1

for i in maze:
    print(i, "\n")


# --------------- creating stack ------------------
def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()

# creating an array to save the path
print('')
print("- DFS search algorithm -")
path = []

# to check the status
found = False

# initializing stating point
m = start_row
n = start_column
start = {m: n}
current = {m: n}

# adding starting point to the path
path.append(start)

push(stack, (start))

first_search = maze[m][n-1]

second_search = maze[m-1][n]

third_search = -1
if m<5:
    third_search = maze[m + 1][n]

fourth_search = -1
if n < 5:
    fourth_search = maze[m][n + 1]

fifth_search = -1
if m < 5 and n > 0:
    fifth_search = maze[m+1][n-1]

sixth_search = -1
if n > 0 and m > 0:
    sixth_search = maze[m-1][n-1]

seventh_search = -1
if n < 5 and m > 0:
    seventh_search = maze[m-1][n+1]

eighth_search = -1
if n < 5 and m < 5:
    eighth_search = maze[m+1][n+1]

a = 0
while (a < 36):
    if (first_search == 0 or first_search == 8) and (n!=0):
        if (maze[m][n-1] == 8):
            print("path found")
            m = m
            n = n - 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m][n - 1] = -1
        m = m
        n = n - 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m < 5:
            third_search = maze[m + 1][n]
        if n < 5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (second_search == 0 or second_search == 8) and (m!=0):
        if (maze[m - 1][n] == 8):
            print("path found")
            m = m - 1
            n = n
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m - 1][n] = -1
        m = m - 1
        n = n
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n < 5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (third_search == 0 or third_search == 8) and (m!=5):
        if (maze[m + 1][n] == 8):
            print("path found")
            m = m + 1
            n = n
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m + 1][n] = -1
        m = m + 1
        n = n
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n < 5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (fourth_search == 0 or fourth_search == 8) and (n!=5):
        if (maze[m][n+1] == 8):
            print("path found")
            m = m
            n = n + 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m][n + 1] = -1
        m = m
        n = n + 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n<5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (fifth_search == 0 or fifth_search == 8) and (m != 5 and n != 0):
        if (maze[m+1][n-1] == 8):
            print("path found")
            m = m + 1
            n = n - 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m + 1][n - 1] = -1
        m = m + 1
        n = n - 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n<5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (sixth_search == 0 or sixth_search == 8) and (m != 0 and n != 0):
        if (maze[m-1][n-1] == 8):
            print("path found")
            m = m - 1
            n = n - 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m - 1][n - 1] = -1
        m = m - 1
        n = n - 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n<5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (seventh_search == 0 or seventh_search == 8) and (m != 0 and n != 5):
        if (maze[m-1][n+1] == 8):
            print("path found")
            m = m - 1
            n = n + 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m - 1][n + 1] = -1
        m = m - 1
        n = n + 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n<5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    elif (eighth_search == 0 or eighth_search == 8) and (m != 5 and n != 5):
        if (maze[m+1][n+1] == 8):
            print("path found")
            m = m + 1
            n = n + 1
            current = {m: n}
            path.append(current)
            found = True
            break
        maze[m + 1][n + 1] = -1
        m = m + 1
        n = n + 1
        current = {m: n}
        push(stack, (current))
        path.append(current)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m<5:
            third_search = maze[m + 1][n]
        if n<5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]
        a += 1

    else:
        pop(stack)
        current = {}
        for i in stack:
            current = i
        m = list(current.keys())[0]
        n = current.get(m)
        first_search = maze[m][n - 1]
        second_search = maze[m - 1][n]
        if m < 5:
            third_search = maze[m + 1][n]
        if n < 5:
            fourth_search = maze[m][n + 1]
        if m < 5 and n > 0:
            fifth_search = maze[m + 1][n - 1]
        if n > 0 and m > 0:
            sixth_search = maze[m - 1][n - 1]
        if n < 5 and m > 0:
            seventh_search = maze[m - 1][n + 1]
        if n < 5 and m < 5:
            eighth_search = maze[m + 1][n + 1]

print("path : ", path)
print("stack : ", stack)

if (found == True):
    time = len(path)
    print('Time to find the goal : ' + str(time) + ' minutes')

def reEstablishMaze():
    for x in range(0, 6):
        for y in range(0, 6):
            if (maze[x][y] == -1):
                maze[x][y] = 0

reEstablishMaze()

def heuristic_cost():
    count_y = 0
    gy = end_row
    gx = end_column
    global heuristic_val
    heuristic_val = {}
    while (count_y < 6):
        count_x = 0
        while (count_x < 6):
            h_cost = max(abs(count_x - gx), abs(count_y - gy))
            heuristic_val[count_y,count_x] = h_cost
            # print('heusristic cost for ' + str(count_y) + ',' + str(count_x) + ' are ' + str(h_cost))
            count_x += 1
        count_y += 1
    print("heuristic costs are : ",heuristic_val)

heuristic_cost()

def astar():
    print('')
    print('- A* search algorithm -')
    m = start_row
    n = start_column

    current = {m: n}
    path = []
    path.append(current)
    gN = 1

    a = 1
    while(a < 36):

        # creating a dictionary to add all relative f costs
        minimum = {}

        # calculating f cost
        if (n != 0) and (maze[m][n - 1] == 0 or maze[m][n - 1] == 8):
            leftHCost = heuristic_val.get((m, n - 1))
            leftFCost = gN + leftHCost
            minimum["left"] = leftFCost
        if (m != 0) and (maze[m - 1][n] == 0 or maze[m - 1][n] == 8):
            topHCost = heuristic_val.get((m - 1, n))
            topFCost = gN + topHCost
            minimum["top"] = topFCost
        if (m != 5) and (maze[m + 1][n] == 0 or maze[m + 1][n] == 8):
            bottomHCost = heuristic_val.get((m + 1, n))
            bottomFCost = gN + bottomHCost
            minimum["bottom"] = bottomFCost
        if (n != 5) and (maze[m][n + 1] == 0 or maze[m][n + 1] == 8):
            rightHCost = heuristic_val.get((m, n + 1))
            rightFCost = gN + rightHCost
            minimum["right"] = rightFCost
        if (m != 5 and n != 0) and (maze[m+1][n-1] == 0 or maze[m+1][n-1] == 8):
            bottomleftHCost = heuristic_val.get((m+1, n - 1))
            bottomleftFCost = gN + bottomleftHCost
            minimum["bottomleft"] = bottomleftFCost
        if (m != 0 and n != 0) and (maze[m-1][n-1] == 0 or maze[m-1][n-1] == 8):
            topleftHCost = heuristic_val.get((m-1, n - 1))
            topleftFCost = gN + topleftHCost
            minimum["topleft"] = topleftFCost
        if (m != 0 and n != 5) and (maze[m-1][n+1] == 0 or maze[m-1][n+1] == 8):
            toprightHCost = heuristic_val.get((m-1, n + 1))
            toprightFCost = gN + toprightHCost
            minimum["topright"] = toprightFCost
        if (m != 5 and n != 5) and (maze[m+1][n+1] == 0 or maze[m+1][n+1] == 8):
            bottomrightHCost = heuristic_val.get((m+1, n + 1))
            bottomrightFCost = gN + bottomrightHCost
            minimum["bottomright"] = bottomrightFCost

        minimum_f_cost = min(minimum, key=minimum.get)

        if (minimum_f_cost == "left"):
            maze[m][n] = -1
            m = m
            n = n - 1
            current = {m: n}
            path.append(current)
            a += 1
            if(maze[m][n]==8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "top"):
            maze[m][n] = -1
            m = m - 1
            n = n
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "bottom"):
            maze[m][n] = -1
            m = m + 1
            n = n
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "right"):
            maze[m][n] = -1
            m = m
            n = n + 1
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "bottomleft"):
            maze[m][n] = -1
            m = m + 1
            n = n - 1
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "topleft"):
            maze[m][n] = -1
            m = m - 1
            n = n - 1
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "topright"):
            maze[m][n] = -1
            m = m - 1
            n = n + 1
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

        elif (minimum_f_cost == "bottomright"):
            maze[m][n] = -1
            m = m + 1
            n = n + 1
            current = {m: n}
            path.append(current)
            a += 1
            if (maze[m][n] == 8):
                print('path found !')
                print(path)
                break

    time = len(path)
    print('Time to find the goal : ' + str(time) + ' minutes')

astar()
