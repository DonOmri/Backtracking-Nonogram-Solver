###########################################################
# FILE : ex8.py
# WRITER : Omri Aviv, omriaviv, 315817403, Leora Lipsky, leoral, 208783357
# EXERCISE : intro2cse ex8 2021
# DESCRIPTION: A program that solves nonogram game
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
###########################################################

from typing import Optional, Union
import copy

FULL_SQUARE = 1
EMPTY_SQUARE = 0
UNKNOWN_SQUARE = -1


def constraint_satisfactions(n: int, blocks: list) -> Optional[list]:
    """This function calls _helper on row made solely from UNKNOWN_SQUARE"""

    empty_row = [UNKNOWN_SQUARE for _ in range(n)]
    options_list = _helper(empty_row, blocks, [], [], len(blocks))
    return options_list


def row_variations(row: list, blocks: list) -> Optional[list]:
    """This function calls _helper function on a mixed row, contains both
    FULL_SQUARE, EMPTY_SQUARE and UNKNOWN_SQUARE"""

    options_list = _helper(row, blocks, [], [], len(blocks))
    return options_list


def _helper(row: list, blocks: list, candidate: list, options_list: list,
            blocks_left: int) -> Optional[list]:
    """This function searches for existence of blocks constraints inside a
    given row, then returns all possibilities."""

    # Base cases:

    # 1. The current candidate pattern does not match the given row.
    for index in range(len(candidate)):
        if row[index] == EMPTY_SQUARE and candidate[index] == FULL_SQUARE or \
                row[index] == FULL_SQUARE and candidate[index] == EMPTY_SQUARE:
            return

    # 2. All block indexes have been added to n. Now check if the row contains
    # any more full squares. if True - candidate can't exist. if False, append
    # empty squares in the remaining indexes of candidate.
    if blocks_left == 0:
        if len(candidate) < len(row):
            for remains in range(len(candidate) - 1, len(row)):
                if row[remains] == FULL_SQUARE:
                    return options_list

        zeros_added = 0

        # Append extra 0's to match n length, then remove them.
        for i in range(len(row) - len(candidate)):
            candidate.append(EMPTY_SQUARE)
            zeros_added += 1
        options_list.append(candidate[:])
        for j in range(zeros_added):
            candidate.pop()
        return options_list

    # 3. The remaining length of n is not long enough to append rest of block
    # indexes, therefore it cannot be a solution, and we should retreat.
    if len(candidate) + sum(blocks) + len(blocks) - 1 > len(row):
        return options_list

    # Recursive cases:

    # 1. Append 0 at the current index
    _helper(row, blocks, candidate + [EMPTY_SQUARE], options_list, blocks_left)

    # 2. Append 1 to the next block[0] indexes of n
    for j in range(blocks[0]):
        candidate.append(FULL_SQUARE)
    if len(candidate) < len(row):
        _helper(row, blocks[1:], candidate + [EMPTY_SQUARE], options_list,
                blocks_left - 1)
    else:
        _helper(row, blocks[1:], candidate, options_list, blocks_left - 1)

    candidate = candidate[:-blocks[0]]

    return options_list


def intersection_row(rows: list) -> Optional[list]:
    """This function combines all results from _helper function to form one
     final row contains only valid (found on all given rows) indexes."""

    if not rows:
        return
    # This section creates the given rows as lists for each of their indexes
    # (indexes 0 from all the rows in one new list).
    all_indexes_list = from_row_to_col(rows)

    # This section checks if all inner indexes of an index are identical.
    # If so, append that index value (full or empty square) to the final
    # solution. If not, append UNKNOWN_SQUARE.
    solution = [UNKNOWN_SQUARE if index[0] == UNKNOWN_SQUARE or index.count(
        index[0]) != len(index) else index[0] for index in all_indexes_list]

    return solution


def solve_easy_nonogram(constraints: list) -> list:
    """This function attempts to solve a nonogram game, and returns the answer,
     whether it succeeded or the board still contains UNKNOWN_SQUARES"""

    # This section creates the board as len(constraints[0]) number of rows,
    # each contains len(constraints[1]) times UNKNOWN_SQUARE
    temp_board = [[UNKNOWN_SQUARE for _ in range(len(constraints[1]))]
                  for _ in range(len(constraints[0]))]

    solved_board = _sen_helper(temp_board, constraints[0], constraints[1])

    return solved_board


def _sen_helper(temp_board: list, row_cons: list, col_cons: list) -> \
        Optional[list]:
    """This function iterates through all rows and cols of a given temp_board,
     and updates them according to results from called functions."""

    old_counter = len(row_cons) * len(col_cons)
    new_counter = 0

    while any(UNKNOWN_SQUARE in row for row in temp_board):

        # Searches the board rows for results, depending on given constraints.
        for index, row in enumerate(temp_board):
            if UNKNOWN_SQUARE in row:
                possible_rows = _helper(row, row_cons[index], [], [],
                                        len(row_cons[index]))
                if possible_rows:
                    final_row = intersection_row(possible_rows)
                    temp_board[index] = final_row
                else:
                    return None

        # Creates board as list of cols
        cols_temp_board = from_row_to_col(temp_board)

        # Searches the board cols for results, depending on given constraints.
        # index == 0 stands for forcing 1st iteration through col
        for index, col in enumerate(cols_temp_board):
            if UNKNOWN_SQUARE in col or old_counter == \
                    len(row_cons) * len(col_cons):
                possible_cols = _helper(col, col_cons[index], [], [],
                                        len(col_cons[index]))
                if possible_cols:
                    final_col = intersection_row(possible_cols)
                    for j in range(len(temp_board)):
                        if temp_board[j][index] == UNKNOWN_SQUARE:
                            temp_board[j][index] = final_col[j]
                else:
                    return None

        # This section compares between amounts of UNKNOWN_SQUARES
        for row in temp_board:
            new_counter += row.count(UNKNOWN_SQUARE)

        if new_counter == old_counter:
            break
        else:
            old_counter = new_counter
            new_counter = 0

    return temp_board


def validate_input(row_cons: list, col_cons: list) -> Union[list, bool]:
    """This function checks if the constraints input is valid."""

    # Checks if an empty block constraint was given as [0] instead of []
    if any(0 in row for row in row_cons) or any(0 in col for col in col_cons):
        return []

    # This section checks each row and col for if there are more blocks to fill
    # in that row / col than the length of it.
    for row in row_cons:
        if sum(row) + len(row) - 1 > len(col_cons):
            return []
    for col in col_cons:
        if sum(col) + len(col) - 1 > len(row_cons):
            return []

    return True


def from_row_to_col(rows: list) -> list:
    """This function transfers lists of rows to lists of rows by their index,
     which equals to original rows' columns"""

    col_list = [[rows[j][i] for j in range(len(rows))]
                for i in range(len(rows[0]))]
    return col_list


def solve_nonogram(constraints: list) -> list:
    """This function returns a list of solved nonogram games, or None if
    certain constraints are unsolvable"""

    temp_board = solve_easy_nonogram(constraints)
    if temp_board is None:
        return []
    elif not any(UNKNOWN_SQUARE in row for row in temp_board):
        return [temp_board]
    else:
        return _sn_helper(constraints, temp_board, [])


def _sn_helper(constraints: list, candidate: list, final_list: list) \
        -> Optional[list]:
    """This function solves a nonogram game using backtracking
    and previous functions"""

    # Base case:

    if not any(UNKNOWN_SQUARE in row for row in candidate):
        final_list.append(copy.deepcopy(candidate))
        return

    # Recursive step:

    replaced_index = (0, 0)

    # Find and replace first appearance of UNKNOWN_SQUARE with EMPTY_SQUARE
    for i, row in enumerate(candidate):
        if row.count(UNKNOWN_SQUARE) > 0:
            replaced_index = (i, row.index(UNKNOWN_SQUARE))
            row[replaced_index[1]] = EMPTY_SQUARE
            break

    # Find if theres both row and col with the new block
    if row_variations(candidate[replaced_index[0]],
                      constraints[0][replaced_index[0]]):
        candidate_as_cols = from_row_to_col(candidate)
        if row_variations(candidate_as_cols[replaced_index[1]],
                          constraints[1][replaced_index[1]]):
            _sn_helper(constraints, candidate, final_list)

    # Replace appended EMPTY_SQUARE with FULL_SQUARE
    candidate[replaced_index[0]][replaced_index[1]] = FULL_SQUARE

    # Find if theres both row and col with the new block
    if row_variations(candidate[replaced_index[0]],
                      constraints[0][replaced_index[0]]):
        candidate_as_cols = from_row_to_col(candidate)
        if row_variations(candidate_as_cols[replaced_index[1]],
                          constraints[1][replaced_index[1]]):
            _sn_helper(constraints, candidate, final_list)

    # Replace appended FULL_SQUARE back to UNKNOWN_SQUARE
    candidate[replaced_index[0]][replaced_index[1]] = UNKNOWN_SQUARE

    return final_list
