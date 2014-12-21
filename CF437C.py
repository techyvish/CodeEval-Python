__author__ = 'Vishal'


import sys,math

class Vertex:
    def __init__(self,energy,number):
        self.__energy = energy;
        self.__number = number;

class Graph:
    def __init__(self,graph_dict={}):
        self.__graph_dict = graph_dict;

    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = [];

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2);
        else:
            self.__graph_dict[vertex1] = [vertex2];

    def print_graph(self):
        print self.__graph_dict;

def runprogram():

    sys.stdin  = open("CF437C.txt")
    f = sys.stdin;

    list = f.readline().rstrip('\n').split(" ");
    nodes = int(list[0]);

    vertList = []
    nodeEnergy = f.readline().rstrip('\n').split(" ");

    graph = Graph();
    for i in range(0,nodes):
        v = Vertex(nodeEnergy[i],i+1 )
        vertList.append(v);
        graph.add_vertex(v);

    links = int(list[1]);
    for j in range(0,links):
        edge = f.readline().rstrip('\n').split(" ");
        v1 = vertList[int(edge[0])-1];
        v2 = vertList[int(edge[1])-1];
        graph.add_edge(v1,v2);


def main():
    runprogram()


main()