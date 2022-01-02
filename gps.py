import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


def Erdos_Renyi(N, p):  # Creating Graph based on num of nodes and probability of edges
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            # To avoid repeating of the pairs
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G


def plot_degree_distribution(G):
    degree_sequence = [d for _, d in G.degree()]
    plt.hist(degree_sequence, histtype='step')
    plt.xlabel('Degree $k$')  # The font of the letters is Italic
    plt.ylabel('$P(k)$')
    plt.title('Degree distribution')


def basic_net_stats(G):
    print(f'Number of nodes:{G.number_of_nodes()}')
    print(f'Number of edges:{G.number_of_edges()}')
    degree_sequence = [d for _, d in G.degree()]
    print(f'Average degree:{round(np.mean(degree_sequence), 2)}')
    print(f'Median degree:{round(np.median(degree_sequence), 2)}\n')


# Read file with the same elements on each row
A1 = np.loadtxt('village0.csv', delimiter=',')  # Returns numpy array
A2 = np.loadtxt('village1.csv', delimiter=',')

G1 = nx.to_networkx_graph(A1)  # Coverting adjacency matrix
G2 = nx.to_networkx_graph(A2)  # to graph objects

G1_LCC = max((c for  c in nx.connected_components(G1)), key=len)
G2_LCC = max((G2.subgraph(c) for c in nx.connected_components(G2)), key=len)

plt.figure()
nx.draw(G1_LCC, node_color='lightblue',
        edge_color='gray',
        node_size=20)

plt.figure()
nx.draw(G2_LCC, node_color='lightgreen',
        edge_color='gray',
        node_size=20)

plt.grid(True)
plt.show()