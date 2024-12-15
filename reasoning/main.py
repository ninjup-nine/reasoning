
from reasoning.puzzle.generator import SlidingPuzzleGenerator
from reasoning.puzzle.puzzle import SlidingPuzzle
from reasoning.puzzle.verifier import SlidingPuzzleVerifier
from reasoning.search.algorithms import AStarSearch

def main():
    # Create a generator for 3x3 puzzles
    generator = SlidingPuzzleGenerator(3)
    # Generate a single puzzle
    puzzle = generator.generate(10)
    print("Generated 3x3 puzzle:")
    generator.print_puzzle(puzzle)
    print(f"Solvable: {generator.is_solvable(puzzle)}")

    # Solve the puzzle using A* search
    if generator.is_solvable(puzzle):
        problem = SlidingPuzzle(puzzle)
        solver = AStarSearch(problem)
        result = solver.solve(time_limit=30)  # 30 second time limit
        if result['success']:
            print("\nSolution found!")
            print(f"Steps: {len(result['solution'])}")
            print(f"Nodes generated: {result['nodes_generated']}")
            print(f"Nodes expanded: {result['nodes_expanded']}")
            print(f"Time taken: {result['time']:.2f} seconds")
            # Verify the solution
            verifier = SlidingPuzzleVerifier(problem)
            is_valid = verifier.verify_solution(result['solution'])
            if is_valid:
                print("\nSolution verified successfully!")
                total_cost = verifier.calculate_solution_cost(result['solution'])
                print(f"Total solution cost: {total_cost}")
            else:
                print(f"\nInvalid solution found!")
        else:
            print("\nNo solution found within time limit")
    else:
        print("\nPuzzle is not solvable")

if __name__ == "__main__":
    main()
