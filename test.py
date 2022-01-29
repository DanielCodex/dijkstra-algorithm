from collections import deque
import math
inf = math.inf

distance_from_start = {'E': inf, 'C': inf,
                       'F': inf, 'G': inf, 'D': inf, 'B': inf, 'A': 0}
unvisited_node = {'G', 'E', 'C', 'F', 'D', 'A', 'B'}



previous_node = {'B': 'A', 'F': 'D', 'A': None,
                 'D': 'A', 'G': 'E', 'C': 'A', 'E': 'D'}

# when we want to reconstruct the path, we are going to use this hash table
prev_node = {'G': None, 'A': None, 'E': None, 'D': None, 'B': None, 'C': None, 'F': None}

adjacency_list = {'B': {('E', 4.0), ('C', 6.0)}, 'G': set(), 'D': {('F', 2.0), ('E', 2.0)}, 'F': {('G', 5.0)}, 'A': {
    ('B', 5.0), ('C', 3.0), ('D', 6.0)}, 'E': {('F', 4.0), ('G', 3.0)}, 'C': {('D', 7.0), ('E', 6.0)}}

print(adjacency_list['A'])

while unvisited_node:
    # each loop we will take the lower cost node 
    current_node = min(
        unvisited_node, key=lambda node: distance_from_start[node]
    )
    # then we will remove it
    unvisited_node.remove(current_node)

    # if current distance(cost) is infinity, the remaining node are not connected 
    # so we are done
    if distance_from_start[current_node] == inf:
        break

    for neighbour, distance in adjacency_list[current_node]:
        new_path = distance_from_start[current_node] + distance

        if new_path < distance_from_start[neighbour]:
            print(distance_from_start)
            distance_from_start[neighbour] = new_path # aka cost
            previous_node[neighbour] = current_node
    
    end_node = "G"
    if current_node == end_node:
        break

    # print(distance_from_start)
    


# path = deque()
# current_node = "G"
# while previous_node[current_node] is not None:
#     path.appendleft(current_node)
#     current_node = previous_node[current_node]
# path.appendleft("A")

# print(list(path))


