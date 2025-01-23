
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, List

S = TypeVar('S')  # State type
A = TypeVar('A')  # Action type

@dataclass
class SearchNode(Generic[S, A]):
    """A single node in a search tree."""
    state: S
    action: Optional[A]  # Action that led to this state (None for root)
    parent: Optional['SearchNode[S, A]']  # Parent node (None for root)
    path_cost: float  # Cost from start to this node
    depth: int  # Depth in the search tree
    count: int = 0  # Unique counter for tie-breaking

    def __lt__(self, other: 'SearchNode[S, A]') -> bool:
        # This is used by heapq for comparing nodes
        return self.count < other.count

    def get_path(self) -> List[A]:
        """Reconstruct path of actions from root to this node."""
        path = []
        current = self
        while current.parent is not None:
            path.append(current.action)
            current = current.parent
        return list(reversed(path))
