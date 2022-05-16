class Graph:
    """
    English version of a simple Graph, with some speed-ups
    but still using Edge
    """

    def __init__(self, vertices: int, edges: list):
        self.vertices = vertices
        self.edges = [[] for i in range(vertices+1)]
        for edge in edges:
            self.edges[edge.start].append(edge)

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
