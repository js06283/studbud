#Groups students based on similarity of study habits and preferences

import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import networkx as nx
import nxmetis
import scipy as sp


names =['name','q1','q2','q3','q4','q5']
dataset = pd.read_csv('test.csv',names=names)
size = dataset.shape[0]
print(size)
dataset['combine'] = dataset.apply(lambda row: [row[1],row[2],row[3],row[4],row[5]], axis = 1)
questions = dataset['combine'].tolist()

#Nearest Neighbors Classifier Graph
classifier = NearestNeighbors(n_neighbors = 3)
classifier.fit(questions)
A = classifier.kneighbors_graph(X = questions, mode = 'connectivity')

#Convert graph to NetworkX
G = nx.from_scipy_sparse_matrix(A)
print(G.nodes())
print(G.edges())

#Partition the graph into groups of approximately 4
group_num = size//4
G2 = nxmetis.partition(G, group_num)

groups = G2[1]

#Match values back to names
groups_final = []
for group in groups:
    group_names = []
    for pers in group: 
        name = dataset.loc[pers,'name']
        group_names.append(name)
    groups_final.append(group_names)

group_data = pd.DataFrame(groups_final)
group_data.to_csv('course_groups.csv')
print(groups_final)




  