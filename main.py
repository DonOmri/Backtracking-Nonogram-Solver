    row_as_not_zero, blocks_as_ones = _rv_comparator(row, blocks)
    _row_variations_helper(row_as_not_zero, blocks_as_ones, [])
    return row_as_not_zero, blocks_as_ones


print(constraint_satisfactions(11, [1,2,1]))
###################################################################################################################
def _row_variations_helper(row_as_not_zero, blocks_as_ones, options_list):
    """Purpose: get back all options for possible combinations of blocks inside
         given row, considering the exist data
         row: list of 1s, 0s and -1s, representing a row in m*n nonogram matrix
         blocks: list of sizes of 1 that should be inside the row
         """

    """base cases:
     1. all blocks have been added
     2. the pattern of the row isn't suitable for at least on of the blocks,
      by their order"""

    # The space u need to place all blocks + a 0 between each is larger than
    # what u have on row, therefore this case cannot exist
    if not sum(blocks) + len(blocks) - 1 > len(
            row):  # CHANGE THIS TO MATCH THE NEW PASSED PARAMETERS
        options_list.append("successful recursion")

    if _rv_comparator(row, blocks) is None:
        # No arrangement is possible -> what should be printed out?
        pass

    # TODO: ph, need to write recursive code here


###################################################################################################################

# TODO: explain this function and its parts a lot better
def _rv_comparator(row, blocks):
    """This function checks whether its possible for a given blocks
     combination to match given row pattern. it creates the blocks as sequences
      of ones, and rows as sequences of 1s and -1s, then compares between"""

    # This section creates two lists: one creates 'blocks' as list of lists of
    # 1s, the other creates list of lists of non 0's from 'row' variable
    row_as_not_zero = []
    sequence_not_zero = []
    for i in row:
        if i == 0:
            if sequence_not_zero:
                row_as_not_zero.append(sequence_not_zero[:])
            sequence_not_zero = []
        else:
            sequence_not_zero.append(i)

    if sequence_not_zero:
        row_as_not_zero.append(sequence_not_zero[:])

    blocks_as_ones = []
    for j in blocks:
        sequence_of_one = []
        for i in range(j):
            sequence_of_one.append(FULL_SQUARE)
        blocks_as_ones.append(sequence_of_one)

    # MAYBE GO FROM HERE BACK TO ORIGINAL FUNCTION, THEN TO HELPER, THEN GO RECURSIVE ON THE REST?
    # OR IS IT INEFFICIENT?

    # create a modular helepr to test first assignment as n long list of -1, then somehow implement a list of 1s and -1s.

    # This section checks if there's a way to insert blocks_as_ones in
    # row_as_not_zero, and returns both created variables if so.

    """print(row_as_not_zero)
    print(blocks_as_ones)"""

    insideable = True
    for k in range(len(row_as_not_zero)):
        for n in range(len(blocks_as_ones)):
            if len(row_as_not_zero[k]) < len(blocks_as_ones[k]):
                insideable = False
                break
            else:  # the blocks_as_row[n] is inside, no need to check how much inside - if theres more room to test blocks_as_row[n+1]
                if len(row_as_not_zero[k]) == len(blocks_as_ones[k]):
                    continue
                else:  # len(row_as_not_zero[k]) < len(blocks_as_ones[k]):
                    insideable = "ph"
                    pass

        if not insideable:
            break

    if insideable:
        print(insideable)


_rv_comparator([1, -1, 0, -1, 0, -1, -1], [3, 1, 2])

"""insideable = True
    counter = 0
    ranz_counter = 0
    for k in range(len(blocks_as_ones)):  # takes each of the blocks_as_ones indexes
        if k+counter > len(row_as_not_zero):
            insideable = False
            break
        for n in range(min(counter,k+counter), len(row_as_not_zero)): # runs any blocks_as_ones indexes on all row_as_not_zeros indexes and see if theres a match # DOES NOT CHECK PROPERLY THE THING I NEED
            if len(blocks_as_ones[k]) > len(row_as_not_zero[n][ranz_counter:]):
                print(len(row_as_not_zero[n][ranz_counter:]))
                print(row_as_not_zero)
                print(n)
                print(ranz_counter)
                insideable = False
            elif len(blocks_as_ones[k]) == len(row_as_not_zero[n][ranz_counter:]):
                counter += 1
                ranz_counter = 0
                break
            else: # if this happens it should run the for loop again with k, not k+1
                ranz_counter += (len(blocks_as_ones[k]) + 1)
                break
        if not insideable:
            break

    if insideable:
        return row_as_not_zero, blocks_as_ones

    return"""

# probably not splitting on 1\-1 when finds a match between block[i] and index
