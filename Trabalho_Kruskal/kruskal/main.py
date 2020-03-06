import pandas as pd
import time
from kruskal import GraphXY
   
g = GraphXY() #instantiate graph
graphs = pd.read_csv('instances/n1500A.txt', sep=" ", header=None). \
                                dropna(axis=1, how='all')
graphs.columns = ["vertex", "x", "y"]

for i in range(len(graphs)):
    g.add_vertex(graphs['vertex'][i], graphs['x'][i], graphs['y'][i])
    
#g.add_vertex(0, 40, 50) -- Optionally, add manually
g.generate_edges()
g.add_weights()
start = time.time()
g.kruskal(sort_method='counting')
end = time.time()
print('\nSeconds taken in Kruskal algorithm: ', end - start)