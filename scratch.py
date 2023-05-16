EX_DATA1 = [[[1, 1, 1, 1, 2, 1, 1, 1, 1], [2], [1, 1, 1, 1, 2, 1, 1, 1, 1],
             [1, 1, 1, 6, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1], [1, 1, 10, 1, 1],
             [1, 1, 2, 1, 1], [1, 14, 1], [1, 2, 1], [18], [2], [1, 2],
             [5, 2, 1], [3, 4, 5], [1, 6, 3], [8, 1]],
            [[1, 8, 1], [1, 2], [1, 6, 1, 4], [1, 1, 2], [1, 4, 1, 1, 1],
             [1, 1, 1, 1], [1, 2, 1, 1, 1, 2], [1, 1, 1, 1, 3], [16], [16],
             [1, 1, 1, 1, 3], [1, 2, 1, 1, 1, 2], [1, 1, 1, 1], [1, 4, 1, 1, 1],
             [1, 1, 2], [1, 6, 1, 4], [1, 2], [1, 8, 1]]]

# For each of these, need to check pdf if this is a possible input
DATA0 = [[[], [3], [2], []], [[1], [2], [2], []]]  # one or more block constraints are empty
DATA1 = [[[], []], [[], [], []]]  # all block constraints are empty - empty board
DATA2 = [[[1], [0], [0], [0]], [[1], [0]]]  # constraint 0 is written as [0] ant not as [] # TODO: FAILED
DATA3 = [[[1, 3], [], [], []], [[1], []]]  # row constraint is longer then row length
DATA4 = [[[1], [], [], []], [[1, 4], []]]  # col constraint is longer then col length
DATA5 = [[[2, 1], [], [1, 2], []], [[2], [], [], []]]  # cols and rows constraints can't exist, but board is solvable only with rows # TODO: NOT WORKING, does not check cols even once
DATA6 = [[[2, 1], [1], [1, 2], []], [[2], [], [], []]]  # cols and rows constraints can't exist and board is reaching col check # TODO: FAILED
DATA7 = [[[2], [2], [1]], [[1], [2], [1, 1]]]  # normal board that only has 1 solution
DATA8 = []  # no data was given at all  # TODO: FAILED
DATA9 = [[[2], [1]]]  # col constraints wasn't given.  # TODO: FAILED
DATA10 = [[[2]], [[1], [1]], [[1]]]  # three constraints were given  # TODO: NOT WORKING. if theres a possibility for a board with only first two constraints, it ignores the 3rd. should it be that way?
DATA11 = [[], []]  # contains 2 empty constraints

row2 = [2,2,2,2,2]
row = [-1, -1, -1, -1, -1]
if row.index(-1) >= 0:
    print(bool(row2.index(-1)))


