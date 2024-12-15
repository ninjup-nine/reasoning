
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

S = TypeVar('S')  # State type
A = TypeVar('A')  # Action type

class Problem(ABC, Generic[S, A]):
    """Abstract base class for defining search problems."""

    @abstractmethod
    def initial_state(self) -> S:
        """Return the initial state."""
        pass

    @abstractmethod
    def is_goal(self, state: S) -> bool:
        """Return True if state is a goal state."""
        pass

    @abstractmethod
    def actions(self, state: S) -> List[A]:
        """Return list of available actions in state."""
        pass

    @abstractmethod
    def result(self, state: S, action: A) -> S:
        """Return the state that results from taking action in state."""
        pass

    @abstractmethod
    def step_cost(self, state: S, action: A, next_state: S) -> float:
        """Return the cost of taking action in state to reach next_state."""
        pass

    def heuristic(self, state: S) -> float:
        """Estimate of cost from state to nearest goal. Default: optimistic 0."""
        return 0.0

class Verifier(Generic[S, A]):
    """Abstract base class for solution verifiers."""

    def __init__(self, problem: Problem[S, A]):
        self.problem = problem

    @abstractmethod
    def verify_solution(self, solution: List[A]) -> bool:
        """Verify if the solution is valid."""
        pass

    @abstractmethod
    def calculate_solution_cost(self, solution: List[A]) -> float:
        """Calculate the total cost of the solution."""
        pass
