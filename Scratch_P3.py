#%%
import numpy as np
import networkx as nx

# %%
A = [[0,3,6,5],[3,0,5,6],[6,5,0,3],[5,6,3,0]]
# %%
graph = nx.from_numpy_matrix(np.array(A), create_using=nx.Graph)
pos=nx.kamada_kawai_layout(graph)
nx.draw_networkx(graph,pos, labels={ i: str(i+1) for i in range(len(A)) })
nx.draw_networkx_edge_labels(graph,pos,edge_labels=nx.get_edge_attributes(graph,'weight'))
# %%
D = [[0, 3, 6, 5], 
    [3, 0, 5, 6], 
    [6, 5, 0, 3], 
    [5, 6, 3, 0]]
graphD = nx.from_numpy_matrix(np.array(D), create_using=nx.Graph)
posD=nx.kamada_kawai_layout(graphD)
mst = nx.algorithms.tree.mst.minimum_spanning_tree(graphD)
print(mst.size(weight='weight'))
# %%
from math import comb
s = 0
for i in range(26):
    s += comb(25,i)
    print(i, ":", s)
# %%
A = [   [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]]

graph = nx.from_numpy_matrix(np.array(A), create_using=nx.Graph)
pos=nx.kamada_kawai_layout(graph)
nx.draw_networkx(graph,pos, labels={ i: str(i+1) for i in range(len(A)) })
nx.draw_networkx_edge_labels(graph,pos,edge_labels=nx.get_edge_attributes(graph,'weight'))

# %%
result = nx.linalg.algebraicconnectivity.fiedler_vector(graph)
print(result)
norm = np.linalg.norm(result)
print(norm)
# %%
np.sum(result**2)

# %%
