def paths_with_obstacles(A):
    """Finds unique paths from top left to bottom right through given matrix,
       A, where 0 is clear and obstacle is 1. Can only move right and down."""

    paths = [[0] * len(A[0]) for i in A] # replicates A with all 0's

    # starting square, 1 way to get there
    if A[0][0] == 0:
        paths[0][0] = 1

    # now we go through A checking if clear, and adding num of routes in paths
    """len(A) = x  len(A[0]) = y"""

    # start with top row
    for x in range(1, len(A)):
        if A[x][0] == 0:
            paths[x][0] = paths[x - 1][0]
            # for these we're just copying the left value if the cell isn't blocked


    # then fill left column
    for y in range(1, len(A[0])):
        if A[0][y] == 0:
            paths[0][y] = paths[0][y - 1]

    # now that the borders are established, fill in middle by adding the neighbor cells
    # current constraint is can only move right and down, so just add left and upper cells
    for x in range(1, len(A)):
        for y in range(1, len(A[0])):
            if A[x][y] == 0:
                paths[x][y] = paths[x - 1][y] + paths[x][y - 1]
                # adding left paths and upper paths

    return paths[-1][-1] # returns count in bottom right cell

print paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print paths_with_obstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print paths_with_obstacles([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])


