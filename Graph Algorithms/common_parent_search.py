import networkx as nx
import matplotlib.pyplot as plt

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': [],
  'F': ['H'],
  'G': ['I'],
  'H': [],
  'I': []
}


def find_common_parent(graph, node1, node2):
    """
    Finds the common parent node of two given nodes in a graph.

    Args:
        graph: A dictionary representation of the graph.
        node1: The first node.
        node2: The second node.

    Returns:
        The common parent node of node1 and node2, or None if there is no common parent.
    """

    
    stack = [node1]
    parents = set()

    #find all of node1 parents
    while stack:
        node = stack.pop()
        for parent, children in graph.items():
            if node in children:
                parents.add(parent)
                stack.append(parent)
    
    #find all of node2 parents
    parents2 = set()
    stack = [node2]
    while stack:
        node = stack.pop()
        for parent, children in graph.items():
            if node in children:
                parents2.add(parent)
                stack.append(parent)
    
    #Find the intersection of the two parents
    common_parent = parents.intersection(parents2)

    return common_parent
    
print(find_common_parent(graph, 'F', 'G'))

# # Create a NetworkX graph object
# G = nx.Graph()

# # Add nodes and edges to the graph
# for node in graph:
#     G.add_node(node)

# for node, neighbors in graph.items():
#     for neighbor in neighbors:
#         G.add_edge(node, neighbor)

# # Visualize the graph
# nx.draw(G, with_labels=True)
# plt.show()