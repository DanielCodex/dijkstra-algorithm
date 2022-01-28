from collections import deque
import math
inf = math.inf

distance_from_start = {'E': inf, 'C': inf,
                       'F': inf, 'G': inf, 'D': inf, 'B': inf, 'A': 0}
unvisited_node = {'G', 'E', 'C', 'F', 'D', 'A', 'B'}


current_node = min(
    unvisited_node, key=lambda node: distance_from_start[node]
)

previous_node={'B': 'A', 'F': 'D', 'A': None, 'D': 'A', 'G': 'E', 'C': 'A', 'E': 'D'}

path = deque()
current_node = "G"
while previous_node[current_node] is not None:
    path.appendleft(current_node)
    current_node = previous_node[current_node]
path.appendleft("A")

print(list(path))