
import time
from typing import Generic, Optional, TypeVar, Dict, Any, Set, List
from heapq import heappush, heappop
from .node import SearchNode
from .problem import Problem
from abc import ABC, abstractmethod

S = TypeVar('S')  # State type
A = TypeVar('A')  # Action type

class SearchAlgorithm(Generic[S, A], ABC):
    """Base class for search algorithms."""

    def __init__(self, problem: Problem[S, A]):
        self.problem = problem
        self.nodes_generated = 0  # Total nodes discovered
        self.nodes_expanded = 0  # Total nodes visited

    def solve(self, time_limit: Optional[float] = None, node_limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Run search algorithm and return results dictionary containing:
        - 'success': Whether a solution was found
        - 'solution': List of actions if found, None otherwise
        - 'nodes_generated': Total nodes generated
        - 'nodes_expanded': Total nodes expanded
        - 'time': Time taken in seconds
        """
        start_time = time.time()
        initial_node = SearchNode(
            state=self.problem.initial_state(),
            action=None,
            parent=None,
            path_cost=0,
            depth=0
        )
        result = self._search(
            initial_node,
            start_time,
            time_limit,
            node_limit
        )
        end_time = time.time()
        return {
            'success': result is not None,
            'solution': result.get_path() if result else None,
            'nodes_generated': self.nodes_generated,
            'nodes_expanded': self.nodes_expanded,
            'time': end_time - start_time
        }

    @abstractmethod
    def _search(
        self,
        initial_node: SearchNode[S, A],
        start_time: float,
        time_limit: Optional[float],
        node_limit: Optional[int]
    ) -> Optional[SearchNode[S, A]]:
        """Implementation of the actual search algorithm."""
        pass

class AStarSearch(SearchAlgorithm[S, A]):
    """A* search algorithm implementation."""

    def _search(
        self,
        initial_node: SearchNode[S, A],
        start_time: float,
        time_limit: Optional[float],
        node_limit: Optional[int]
    ) -> Optional[SearchNode[S, A]]:
        # Add counter for unique node IDs
        node_counter = 0
        initial_node.count = node_counter
        frontier = []  # Priority queue
        heappush(frontier, (0, initial_node))  # Priority = f(n) = g(n) + h(n)
        explored: Set[Any] = set()  # Set of explored states
        self.nodes_generated = 1
        self.nodes_expanded = 0

        while frontier:
            if time_limit and (time.time() - start_time) >= time_limit:
                return None
            if node_limit and self.nodes_generated >= node_limit:
                return None

            # Get node with lowest f-value
            f, node = heappop(frontier)
            if self.problem.is_goal(node.state):
                return node

            state_tuple = self._state_to_tuple(node.state)
            if state_tuple not in explored:
                explored.add(state_tuple)
                self.nodes_expanded += 1
                for action in self.problem.actions(node.state):
                    next_state = self.problem.result(node.state, action)
                    next_state_tuple = self._state_to_tuple(next_state)
                    if next_state_tuple not in explored:
                        step_cost = self.problem.step_cost(
                            node.state, action, next_state
                        )
                        node_counter += 1  # Increment counter for new node
                        child = SearchNode(
                            state=next_state,
                            action=action,
                            parent=node,
                            path_cost=node.path_cost + step_cost,
                            depth=node.depth + 1,
                            count=node_counter  # Assign unique counter
                        )
                        f = child.path_cost + self.problem.heuristic(next_state)
                        heappush(frontier, (f, child))
                        self.nodes_generated += 1
        return None  # No solution found

    def _state_to_tuple(self, state: S) -> Any:
        """Helper method to convert state to a hashable tuple."""
        # This method may need to be customized based on state representation
        return tuple(tuple(row) for row in state)  # For 2D lists
