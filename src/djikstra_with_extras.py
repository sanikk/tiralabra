from heapq import heappop, heappush
# varmaan tarpeeton, ei tän tartte noita ymmärtää, kunhan käyttää
# from entities.Verkko import Kaari, Verkko
from entities.Graph import Edge, Graph
from ui.mock_gui import Mock_Gui


def djikstra(graph: Graph, start, end=-1, GUI=Mock_Gui()):
    # -1 means inf. here, 0 index is never used (i hope!)
    handled = [False for i in range(graph.vertices + 1)]

    # no dicts here, just list+index, see https://wiki.python.org/moin/TimeComplexity
    # handled = {n: False for n in range(graph.vertices + 1)}

    distances = [-1 for i in range(graph.vertices + 1)]
    distances[start] = 0
    heap = []
    heappush(heap, (0, start))
    round = 1
    while len(heap) > 0:
        # is this dist total distance to vertex or...seems like total. CHECK AFTER LUNCH - TODO
        dist, vertex = heappop(heap)
        if end != -1 and vertex == end:
            return distances[end]
        if handled[vertex]:
            continue
        handled[vertex] = True
        for edge in graph.give_edges(vertex):
            # this should already be the shortest length ? check!! TODO
            if not handled[edge.end]:
                dist_old = distances[edge.end]
                # CHECK THIS!! - TODO
                new_dist = distances[edge.start] + \
                    edge.weight  # 'edge.start == vertex' here
                # but is distances[edge.start] == dist ?
                if dist_old == -1 or new_dist < dist_old:
                    distances[edge.end] = new_dist
                    heappush(heap, (new_dist, edge.end))
        # For updating GUI for the visualization
        GUI.update_gui(round, len(heap), handled, distances)
        round += 1
    # return distance from (start) to (last_)
    return distances[-1]
