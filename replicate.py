# repliate dij_other
# this code and dijkstra_algorithm are perfect for learning
import math

graph = {
    'a': {'b': 3, 'c': 4, 'd': 7},
    'b': {'c': 1, 'f': 5},
    'c': {'f': 6, 'd': 2},
    'd': {'e': 3, 'g': 6},
    'e': {'g': 3, 'h': 4},
    'f': {'e': 1, 'h': 8},
    'g': {'h': 2},
    'h': {'g': 2}
}

def dijkstra(graph, start, goal):
    infinity = math.inf

    unseenNodes = graph
    shortest_distance = {} # we will update this mostly
    track_predecessor = {} # like prev_node
    track_path = [] # for not checking same place twice

    # first show me all of the deatil
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None 

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            new_cost = shortest_distance[min_distance_node] + weight 

            if new_cost < shortest_distance[child_node]:
                shortest_distance[child_node] = new_cost
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)
    
    currentNode = goal 
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('it is not reachable')
            break
    track_path.insert(0, start)



print(dijkstra(graph, "a", "h"))
