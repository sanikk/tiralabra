class Graph:
    """
    A simple Graph, with some speed-ups but still using Edge
    """

    def __init__(self, vertices: int, edges: list):
        self.vertices = vertices
        self.edges = [[] for i in range(vertices+1)]
        self.number_of_edges = len(edges)
        self.transform_edges(edges)

    def transform_edges(self, edges):
        """ added this for heuristic-function
        """
        summa = 0
        for edge in edges:
            self.edges[edge.start].append(edge)
            summa += edge.weight
        self.average_weight = summa / len(edges)

    def give_edges(self, vertex):
        if vertex < 1 or vertex > self.vertices:
            raise ValueError
        return self.edges[vertex]


class Edge:
    """ class for representing Edges between two points.

    Done with namedtuples using __slots__

    """
    __slots__ = ['start', 'end', 'weight']

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    """ class for simulating vertices that know their neighbors, and distance (weight)
    to those neighbors
    """

    def __init__(self, name, neighbors: list):
        """ neighbors is intended to be a list of (vertex, weight) tuples
        name can be int or str, or whatever
        """
        self.name = name  # so they can tell where it's at now
        self.neighbors = neighbors

    def give_neighbors(self):
        return self.neighbors
