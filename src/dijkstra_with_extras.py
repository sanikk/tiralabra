from heapq import heappop, heappush
from entities.graph import Edge, Graph
from ui.mock_gui import Mock_Gui


def dijkstra(graph: Graph, start, end=-1, GUI=Mock_Gui()):
    # -1 means inf. here, 0 index is never used (i hope!)
    handled = [False for i in range(graph.vertices + 1)]

    # no dicts here, just list+index, see https://wiki.python.org/moin/TimeComplexity
    # handled = {n: False for n in range(graph.vertices + 1)}

    distances = [-1 for i in range(graph.vertices + 1)]
    distances[start] = 0
    heap = []

    # aliases to speed things up -> lookups in local scope -- TODO TEST THIS!!
    update_ui = GUI.update_dijkstra
    hpush = heappush
    hpop = heappop
    give_edge = graph.give_edges

    hpush(heap, (0, start))
    round = 0

    while len(heap) > 0:
        # dist is total distance to vertex using this path, there might already be a shorter way in distances
        update_ui(round, heap, handled[1:], distances[1:])
        dist, vertex = hpop(heap)
        # print(f'popped {dist=}, {vertex=}')
        if end != -1 and vertex == end:  # this is shortest distance, if there was a shorter way it would have been popped already
            return distances[end]
        if handled[vertex]:
            continue
        handled[vertex] = True
        # fetch next one only once, here.
        dist_here = distances[vertex]
        for edge in give_edge(vertex):
            if not handled[edge.end]:
                dist_old = distances[edge.end]
                new_dist = dist_here + edge.weight
                if dist_old == -1 or new_dist < dist_old:
                    distances[edge.end] = new_dist
                    hpush(heap, (new_dist, edge.end))
        # For updating GUI for the visualization
        #GUI.update_gui(round, len(heap), handled, distances)
        round += 1
    # return distance from (start) to (last_)
    return distances[-1]
