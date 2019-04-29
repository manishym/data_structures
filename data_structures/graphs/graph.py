import sys
import os
import unittest

class Vertex():
    """A vertex of a graph"""
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def __repr__(self):
        return self.__str__()

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        try:
            return self.connectedTo[nbr]
        except KeyError as e:
            return None


class Graph():
    """The Graph ADT"""
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def __contains__(self, n):
        return n in vertList

    def addEdge(self, f, t, cost=0):
        self.addVertex(f)
        self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return list(self.vertList.keys())

    def __iter__(self):
        return iter(self.vertList.values())

    def getVertex(self, key):
        return self.vertList[key]


def main():
    g = Graph()
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 5, 7)
    g.addEdge(2, 4, 5)
    g.addEdge(1, 5, 3)
    g.addEdge(4, 2, 1)
    for v in g:
        for w in v.getConnections():
            print(f"{v} {w.getId()}")

    return

if __name__ == '__main__':
    main()

