import networkx as nx
import math 
import statistics
import matplotlib.pyplot as plt


def average_degree(G):
    node_degree = []
    averageDegree = []
    for n in range(1,30):
        for i in G.nodes():
            node_degree.append(G.degree(i))
            average_deg = statistics.mean(node_degree)
        averageDegree.append(average_deg)
    return statistics.mean(averageDegree)

def average_clustering(G):
    averageClustering = []
    for n in range(1,30):
        clustering = nx.algorithms.cluster.average_clustering(G)
        averageClustering.append(clustering)
    return statistics.mean(averageClustering)

def average_path_length(G):
    averagePathLenght = []
    for n in range(1,30):
        path_length = nx.average_shortest_path_length(G)
        averagePathLenght.append(path_length)    
    return statistics.mean(averagePathLenght)

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
        G = nx.erdos_renyi_graph(n, p)
        print( "The average degree of n" , n ,"and p" ,p ,": ", average_degree(G))
        print( "Average clustering coefficient of n" , n ,"and p" , p ,": " , average_clustering(G))
        print( "The average path length of n" ,n ,"and p" ,p ,": " , average_path_length(G))
        print( "Degree Distribution of n" ,n ,"and p" ,p ,": " , Degree_distribution(G))
            

inputs(100, 0.2)
inputs(200, 0.09)
inputs(300, 0.5)