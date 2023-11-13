from collections import deque


def bfs_search(graph, root):
    """
    Breadth first search algo.
    """

    #visited is the unique set of nodes that we visit
    #queue is the node that is next in line to be searched
    visited, queue = set(), deque([root])

    #initialize the starting point for the search
    visited.add(root)

    #continue search until there are no more nodes (ie queue is empty)
    while queue:
        # remove the first element from the from
        vertex = queue.popleft()
        print(str(vertex), end=" ")

        # iterate through the neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    bfs_search(graph=graph, root=0)
