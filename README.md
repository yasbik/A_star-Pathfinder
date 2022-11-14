# About the Project

This is a program to find the shortest path between two points. It implements the A* pathfinding algorightm and uses visualizer tools in Python to conceptualize how the pathfinding algorithm works.

## The A* Algorithm

[A*](https://en.wikipedia.org/wiki/A*_search_algorithm) is an informed search algorithm, or a [best-first search](https://en.wikipedia.org/wiki/Best-first_search), meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied. As a result, this algorithm is much more efficient than a standard [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) or [breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search).

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes the following formula:

    f(n) = g(n) + h(n)

Here, `n` is the next node on the path, `g(n)` is the cost of the path from the start node to n, and `h(n)` is a [heuristic function](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) that estimates the cost of the cheapest path from n to the goal. A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended. The heuristic function is problem-specific. If the heuristic function is admissible, meaning that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.
