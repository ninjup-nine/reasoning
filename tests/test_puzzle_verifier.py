import pytest
from reasoning.puzzle.puzzle import SlidingPuzzle
from reasoning.puzzle.verifier import SlidingPuzzleVerifier

def test_verify_valid_solution():
    # Simple 2x2 puzzle with solution to reach [[0,1],[2,3]]
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    # Solution to reach goal state [[0,1],[2,3]]
    solution = [
        (0, 1, 0, 0),  # [1,0,2,3] -> [0,1,2,3]
    ]
    
    assert verifier.verify_solution(solution) == True

def test_verify_invalid_action_format():
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    invalid_solution = [
        (0, 1, 0)  # Missing fourth coordinate
    ]
    
    assert verifier.verify_solution(invalid_solution) == False

def test_verify_illegal_move():
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    invalid_solution = [
        (0, 1, 1, 1)  # Trying to move diagonally
    ]
    
    assert verifier.verify_solution(invalid_solution) == False

def test_verify_solution_not_reaching_goal():
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    incomplete_solution = [
        (0, 1, 0, 0),  # Only one move, won't reach goal state
        (0, 0, 1, 0)   # Second move, still not goal state
    ]
    
    assert verifier.verify_solution(incomplete_solution) == False

def test_calculate_solution_cost():
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    solution = [
        (0, 1, 0, 0),
        (0, 0, 1, 0)
    ]
    
    assert verifier.calculate_solution_cost(solution) == 2.0

def test_empty_solution():
    # Initial state that's not the goal state
    initial_state = [
        [1, 0],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    assert verifier.verify_solution([]) == False
    assert verifier.calculate_solution_cost([]) == 0.0

def test_verify_already_solved():
    # Test case where initial state is already the goal state
    initial_state = [
        [0, 1],
        [2, 3]
    ]
    puzzle = SlidingPuzzle(initial_state)
    verifier = SlidingPuzzleVerifier(puzzle)
    
    assert verifier.verify_solution([]) == True
