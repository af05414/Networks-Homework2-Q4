import networkx as nx
import math 
import statistics
import matplotlib.pyplot as plt


def average_degree(G):
    node_degree = []
    for i in G.nodes():
        node_degree.append(G.degree(i))
        average_deg = statistics.mean(node_degree)
    return average_deg

def average_clustering(G):
    clustering = nx.algorithms.cluster.average_clustering(G)
    return clustering

def average_path_length(G):  
    return (nx.average_shortest_path_length(G))

def Degree_distribution(G):
    degrees_dict = {}
    for n in G.nodes():
        degree = G.degree(n)
        if degree not in degrees_dict:
            degrees_dict[degree] = 0
        degrees_dict[degree] += 1
    items = sorted(degrees_dict.items())

    plt.plot([k for (k, v) in items], [v for (k, v) in items])
    
    plt.ylabel("Number of Nodes")
    plt.xlabel('Degree of Nodes)')
    plt.show()
    return items


def inputs(n,p):
    averageDegree = []
    averageClustering = []
    averagePathLenght = []
    for i in range(1,30):
        G = nx.erdos_renyi_graph(n, p)
        avgdeg=average_degree(G)
        avgclus=average_clustering(G)
        apl=average_path_length(G)
        averageDegree.append(avgdeg)
        averageClustering.append(avgclus)
        averagePathLenght.append(apl)
        
    print( "The average degree of n=" , n ,"and p=" ,p ,": ", statistics.mean(averageDegree))
    print( "Average clustering coefficient of n=" , n ,"and p=" , p ,": " , statistics.mean(averageClustering))
    print( "The average path length of n=" ,n ,"and p=" ,p ,": " , statistics.mean(averagePathLenght))
    print( "Degree Distribution of n=" ,n ,"and p=" ,p ,": " , Degree_distribution(G))
            

inputs(100, 0.2)
inputs(200, 0.09)
inputs(300, 0.5)
