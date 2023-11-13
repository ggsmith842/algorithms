"""
Implementation of dijstra's algorithms to find the 
shortest distance in a graph data structure
"""

import sys
from heapq import heapify, heappush


def dijkstra(graph, source, target):
    """
    Pseudocode
    1. Initialize the cost of each node to infinity and source to 0,
       a way to track each node visited, and a pointer starting at the source
    2. You will check each node, so you need a loop that runs n-1 times
       (we don't include the starting point)
    3. If the current node has not been visited add the current node to the visited
    4. Initialize a min heap to keep track of the cost for each neighbor
    5. Visit each neighbor, if the neighbor is not in visited, 
       calculate the cost (cost(current node) + distance_from_node)
    6. Compare the cost to the current cost. 
       If the new cost is less than the current cost, update the cost.
    7. Add the cost to each neighbor to the min heap 
    8. Get the node with the lowest cost and assign it to the pointer temp
    9. Repeat for each node then print the node_data
       for the target to show the imporant information.
    """

    # create inifinity value
    inf = sys.maxsize

    # create dictionary with node costs and predecessor set to track the shortest path
    node_data = {
        "A": {"cost": inf, "pred": []},
        "B": {"cost": inf, "pred": []},
        "C": {"cost": inf, "pred": []},
        "D": {"cost": inf, "pred": []},
        "E": {"cost": inf, "pred": []},
        "F": {"cost": inf, "pred": []},
    }

    # set source cost to 0
    node_data[source]["cost"] = 0

    # initialize visited tracker
    visited = []

    # set temp pointer to source
    temp = source

    # main loop
    # loop through each node (not including the starting node)
    for _ in range(len(graph) - 1):
        # check if we have already visited a node
        if temp not in visited:
            visited.append(temp)

            # create a min_heap to track the cost of each neighbor
            min_heap = []

            # loop through each neighbor to the current node (temp)
            for j in graph[temp]:
                # we don't check nodes/vertices we have already visited
                if j not in visited:
                    # calculate cost (current cost + distance of jth neighbor)
                    cost = node_data[temp]["cost"] + graph[temp][j]

                    # do comparison
                    if cost < node_data[j]["cost"]:
                        # if the calculated cost is less than the current cost, update it
                        node_data[j]["cost"] = cost
                        # for the current neighbor store the current node's predecessors
                        # plus the current node
                        node_data[j]["pred"] = node_data[temp]["pred"] + list(temp)

                    # for each jth neighbor append the cost of each to the heap min_heap
                    heappush(min_heap, (node_data[j]["cost"], j))

        # heapify creates a heap from the min_heap list
        heapify(min_heap)

        # for the minimum value, get the node and assign it to the pointer (temp)
        temp = min_heap[0][1]

    print(f'Shortest Distance: {str(node_data[target]["cost"])}')
    print(f'Shortest Path: {str(node_data[target]["pred"] + list(target))}')

    return -1


if __name__ == "__main__":
    # initialize graph (a dictionary of dictionarys)
    # each key is a vertice/node with the edge value as the value
    GRAPH = {
        "A": {"B": 2, "C": 4},
        "B": {"A": 2, "C": 3, "D": 8},
        "C": {"A": 4, "B": 3, "D": 2, "E": 5},
        "D": {"B": 8, "C": 2, "E": 11, "F": 22},
        "E": {"C": 5, "D": 11, "F": 1},
        "F": {"D": 22, "E": 1},
    }

    # declare and initialize start and target nodes
    SOURCE = "A"
    TARGET = "F"

    # call algorithm
    dijkstra(graph = GRAPH, source=SOURCE, target=TARGET)
