from collections import deque
from typing import Callable


class BFS:
    """Implementations of breadth-first search"""

    @staticmethod
    def bfs_base(graph: dict, start_key: str, function: Callable) -> bool:
        """Basic Breadth First Search"""
        search_queue = deque()
        search_queue += graph[start_key]
        searched = set()

        while search_queue:
            elem = search_queue.popleft()
            if elem not in searched:
                if function(elem):
                    return True
                else:
                    search_queue += graph[elem]
                    searched.add(elem)

        return False


def person_is_seller(name):
    """Example of a function to identify the desired answer"""
    return name[-1] == 'm'


def main() -> None:
    """Tests"""
    friends_graph = {
        "you": ("alice", "bob", "claire"),
        "alice": ("peggy",),
        "bob": ("anuj", "peggy"),
        "claire": ("thom", "jonny"),
        "peggy": tuple(),
        "anuj": tuple(),
        "thom": tuple(),
        "jonny": tuple()
    }

    print(BFS.bfs_base(friends_graph, "you", person_is_seller))


if __name__ == '__main__':
    main()
