import pytest
from reasoning.puzzle.puzzle import SlidingPuzzle

def test_sliding_puzzle_initialization():
    # Test 3x3 puzzle
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(initial_state)
    assert puzzle.size == 3
    assert puzzle.initial_state() == initial_state
    
def test_sliding_puzzle_goal_state():
    # Test goal state detection
    goal_state = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(goal_state)
    assert puzzle.is_goal(goal_state) == True
    
    non_goal_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    assert puzzle.is_goal(non_goal_state) == False

def test_sliding_puzzle_actions():
    # Test valid moves generation
    state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(state)
    actions = puzzle.actions(state)
    
    # Empty tile at (1,1) should have 4 possible moves
    expected_moves = {
        (1, 1, 0, 1),  # up
        (1, 1, 2, 1),  # down
        (1, 1, 1, 0),  # left
        (1, 1, 1, 2)   # right
    }
    assert set(actions) == expected_moves

def test_sliding_puzzle_result():
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(initial_state)
    
    # Test moving tile up
    action = (1, 1, 0, 1)  # Move empty space up
    expected_state = [
        [1, 0, 3],
        [4, 2, 5],
        [6, 7, 8]
    ]
    assert puzzle.result(initial_state, action) == expected_state
    
    # Verify original state wasn't modified
    assert initial_state == [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

def test_sliding_puzzle_heuristic():
    state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(state)
    
    # Calculate expected Manhattan distance
    # In this case, only the empty tile (0) is out of place
    # It should be at (0,0) but is at (1,1)
    # Manhattan distance = |1-0| + |1-0| = 2
    assert puzzle.heuristic(state) == 2.0

def test_sliding_puzzle_step_cost():
    state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(state)
    action = (1, 1, 0, 1)
    next_state = puzzle.result(state, action)
    
    # All moves should have cost 1.0
    assert puzzle.step_cost(state, action, next_state) == 1.0

def test_invalid_puzzle_size():
    # Test with invalid puzzle (not square)
    with pytest.raises(IndexError):
        invalid_state = [
            [1, 2, 3],
            [4, 0]
        ]
        puzzle = SlidingPuzzle(invalid_state)
        puzzle.actions(invalid_state)

def test_puzzle_deep_copy():
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    puzzle = SlidingPuzzle(initial_state)
    
    # Modify original state
    initial_state[0][0] = 9
    
    # Check that puzzle's internal state wasn't affected
    assert puzzle.initial_state() == [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ] 