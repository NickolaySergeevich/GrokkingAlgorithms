class DijkstraAlgorithm:
    """Implementation of Dijkstra's algorithm"""

    @staticmethod
    def dijkstra_algorithm_base(graph: dict) -> dict:
        """Basic implementation of Dijkstra's algorithm"""
        costs = dict()
        parents = dict()
        for key in set(graph) - {"start"}:
            if key in graph["start"]:
                costs[key] = graph["start"][key]
                parents[key] = "start"
            else:
                costs[key] = float("inf")
                parents[key] = None

        processed = set()
        node = DijkstraAlgorithm._find_lowest_cost_node(costs, processed)
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]

            for key in neighbors:
                new_cost = cost + neighbors[key]
                if costs[key] > new_cost:
                    costs[key] = new_cost
                    parents[key] = node

            processed.add(node)
            node = DijkstraAlgorithm._find_lowest_cost_node(costs, processed)

        way = {
            "nodes": ["end"],
            "costs": list(),
            "fin_cost": costs["end"]
        }
        node = "end"
        node_parent = parents[node]
        while node_parent != "start":
            way["nodes"].append(node_parent)
            way["costs"].append(costs[node] - costs[node_parent])

            node = node_parent
            node_parent = parents[node]

        way["nodes"].append("start")
        way["costs"].append(costs[node])

        return way

    @staticmethod
    def _find_lowest_cost_node(costs: dict, processed: set) -> str | None:
        """Finding the node with the lowest cost that has not yet been processed"""
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node


def main() -> None:
    """Tests"""
    graph = {
        "start": {
            'a': 6,
            'b': 2
        },
        'a': {
            "end": 1
        },
        'b': {
            'a': 3,
            "end": 5
        },
        "end": dict()
    }

    way = DijkstraAlgorithm.dijkstra_algorithm_base(graph)
    for key in way:
        print(way[key])


if __name__ == '__main__':
    main()
