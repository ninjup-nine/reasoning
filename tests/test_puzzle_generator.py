import pytest
from typing import List
from reasoning.puzzle.puzzle import SlidingPuzzle
import copy

def count_inversions(state: List[List[int]]) -> int:
    """Helper function to count inversions in puzzle state"""
    # Convert 2D state to 1D list, excluding 0
    flat = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    return inversions

def get_blank_row_from_bottom(state: List[List[int]]) -> int:
    """Helper function to get the row number of blank tile counting from bottom"""
    size = len(state)
    for i in range(size):
        for j in range(size):
            if state[i][j] == 0:
                return size - i - 1
    return -1

def is_solvable(state: List[List[int]]) -> bool:
    """
    Helper function to check if puzzle is solvable
    For 3x3 puzzles:
    - If width is odd, solvable if number of inversions is even
    - If width is even:
        - If blank is on even row from bottom, solvable if inversions is odd
        - If blank is on odd row from bottom, solvable if inversions is even
    """
    size = len(state)
    inversions = count_inversions(state)
    blank_row = get_blank_row_from_bottom(state)
    
    if size % 2 == 1:  # Odd width
        return inversions % 2 == 0
    else:  # Even width
        if blank_row % 2 == 0:  # Even row from bottom
            return inversions % 2 == 1
        else:  # Odd row from bottom
            return inversions % 2 == 0

def test_puzzle_solvability():
    # Test solvable puzzle
    solvable_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    assert is_solvable(solvable_state)
    
    # Test unsolvable puzzle
    unsolvable_state = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]
    assert not is_solvable(unsolvable_state)

def test_puzzle_valid_state():
    # Test that puzzle contains all numbers exactly once
    state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    
    # Check all numbers 0-8 present
    flat = [num for row in state for num in row]
    assert sorted(flat) == list(range(9))
    
    # Test invalid state (duplicate numbers)
    with pytest.raises(AssertionError):
        invalid_state = [
            [1, 2, 3],
            [4, 1, 5],  # 1 appears twice
            [6, 7, 8]
        ]
        puzzle = SlidingPuzzle(invalid_state)

def test_puzzle_size_variations():
    # Test 2x2 puzzle
    state_2x2 = [
        [1, 2],
        [0, 3]
    ]
    puzzle = SlidingPuzzle(state_2x2)
    assert puzzle.size == 2
    
    # Test 4x4 puzzle
    state_4x4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 15]
    ]
    puzzle = SlidingPuzzle(state_4x4)
    assert puzzle.size == 4

def test_edge_case_moves():
    # Test moves when blank is in corner
    corner_state = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(corner_state)
    corner_actions = puzzle.actions(corner_state)
    # Should only have 2 possible moves from corner
    assert len(corner_actions) == 2
    
    # Test moves when blank is on edge
    edge_state = [
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(edge_state)
    edge_actions = puzzle.actions(edge_state)
    # Should have 3 possible moves from edge
    assert len(edge_actions) == 3

def test_multiple_moves():
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(initial_state)
    
    # Make sequence of moves starting with a deep copy of initial state
    state = copy.deepcopy(initial_state)
    
    # Starting from:
    # [1, 2, 3]
    # [4, 0, 5]
    # [6, 7, 8]
    
    moves = [
        (1, 1, 1, 2),  # Move empty right: [1,2,3][4,5,0][6,7,8]
        (1, 2, 0, 2),  # Move empty up: [1,2,0][4,5,3][6,7,8]
    ]
    
    expected_final_state = [
        [1, 2, 0],
        [4, 5, 3],
        [6, 7, 8]
    ]
    
    for move in moves:
        state = puzzle.result(state, move)
        
    assert state == expected_final_state

def test_heuristic_consistency():
    state1 = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(state1)
    h1 = puzzle.heuristic(state1)
    
    # Make one move
    action = (1, 1, 0, 1)
    state2 = puzzle.result(state1, action)
    h2 = puzzle.heuristic(state2)
    
    # Check that difference in heuristics is not greater than cost of move
    assert abs(h1 - h2) <= puzzle.step_cost(state1, action, state2) 