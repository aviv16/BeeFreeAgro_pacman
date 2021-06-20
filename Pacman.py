import numpy as np
from collections import deque


# To store matrix cell coordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source


# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int, max_row, max_col):
    return (row >= 0) and (row < max_row) and (col >= 0) and (col < max_col)


# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell


rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point, max_row, max_col):
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y] != 3 or mat[dest.x][dest.y] != 2:
        return -1

    visited = [[False for i in range(max_col)] for j in range(max_row)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    q = deque()

    # Distance of source cell is 0
    s = queueNode(src, 0)
    q.append(s)  # Enqueue source cell

    # Do a BFS starting from source cell
    while q:

        curr = q.popleft()  # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col, max_row, max_col) and
                    mat[row][col] == 0 and
                    not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col),
                                    curr.dist + 1)
                q.append(Adjcell)

    # Return -1 if destination cannot be reached
    return -1


def pacman_distance_calc(notebook):
    board = np.load(notebook)
    mat = board.tolist()
    pac_location = [np.where(board == 3)[0][0], np.where(board == 3)[1][0]]
    pac_location = Point(pac_location[0], pac_location[1])
    ghosts = np.argwhere(np.array(board) == 2).tolist()
    for ghost in ghosts:
        ghost = Point(ghost[0], ghost[1])
        dist = BFS(board, pac_location, ghost, np.shape(mat)[0], np.shape(mat)[1])
        print(dist)



pacman_distance_calc('board1.npy')
