def answer(map):
    # answer is the length of the final path from the length() method
    finalpath = length(map, 0, 0, True)
    overlay(map, finalpath[1])
    return len(finalpath[1])


def length(map, startr, startc, canBreak):
    # Return type: [HasPath, [path as list of tuples]]

    # If this space doesn't exist, return false
    if(not inboard(map, startr, startc)):
        return [False, None]

    # Base case: we're at the goal.
    # Mark it and return True with the path containing this space only
    if(startr == len(map) - 1 and startc == len(map[0]) - 1):
        map[startr][startc] = '+'
        return [True, [(startr, startc)]]

    # Check for obstacles
    if map[startr][startc] != 0:
        # If we can break and we're at an obstacle, break it
        if(canBreak and map[startr][startc] == 1):
            canBreak = False
            map[startr][startc] = 'X'
        # If we can't break, then we're either at a previous marked spot or
        # an obstacle we can't break
        else:
            return [False, None]

    # Valid space. Mark it.
    if(map[startr][startc] == 0):
        map[startr][startc] = '+'
   
    # Collect valid paths that work
    validdirections = []
    curpos = (startr, startc)
    
    # Check all 4 directions; if they're part of a goal path, add them to the valid list
    right = length(map, startr, startc + 1, canBreak)
    if(right[0] is True):
        right = [True, [curpos] + right[1]]
        validdirections.append(right)

    down = length(map, startr + 1, startc, canBreak)
    if(down[0] is True):
        down = [True, [curpos] + down[1]]
        validdirections.append(down)

    left = length(map, startr, startc - 1, canBreak)
    if(left[0] is True):
        left = [True, [curpos] + left[1]]
        validdirections.append(left)

    up = length(map, startr - 1, startc, canBreak)
    if(up[0] is True):
        up = [True, [curpos] + up[1]]
        validdirections.append(up)

    # If there are no valid directions from current spot (dead end), unmark current path
    if(len(validdirections) == 0):
        unmark(map, [(startr, startc)])
        return [False, None]

    # Otherwise return the shortest path
    else:
        mindir = validdirections[0]
        for direction in validdirections:
            if len(direction[1]) < len(mindir[1]):
                mindir = direction
        unmark(map, mindir[1])
        return mindir


def unmark(map, path):
    for position in path:
        # If it's a normal part of the path, clear it
        if(map[position[0]][position[1]] == '+'):
            map[position[0]][position[1]] = 0
        # If it was broken, set to be an obstacle again
        elif(map[position[0]][position[1]] == 'X'):
            map[position[0]][position[1]] = 1


def inboard(map, r, c):
    # Check if the location is a valid map location
    if((r >= 0 and r < len(map)) and (c >= 0 and c < len(map[0]))):
        return True
    return False

    
def printmap(map):
    for row in map:
        rowstr = ""
        for col in row:
            rowstr += " " + str(col)
        print(rowstr)
    print()


def overlay(map, path):
    for position in path:
        if(map[position[0]][position[1]] == 1):
            map[position[0]][position[1]] = 'X'
        else:
            map[position[0]][position[1]] = '+'
    printmap(map)


maze3 = [[0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0]]
print("Before:")
printmap(maze3)
print("After:")
print(answer(maze3))

