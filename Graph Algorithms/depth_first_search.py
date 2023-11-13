from collections import deque

## recursive
# def df_search(graph, node, visited=None):

#     if visited is None:
#         visited = set()
#     visited.add(node)

#     print(node)

#     stack = graph[node]
#     for next in stack - visited:
#         df_search(graph, next, visited)
    
#     return visited


def df_search(graph, start):

    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
            '1': set(['0', '3', '4']),
            '2': set(['0']),
            '3': set(['1']),
            '4': set(['2', '3'])}

    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    
    print(df_search(graph, 'A'))

    