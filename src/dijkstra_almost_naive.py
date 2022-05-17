from heapq import heappop, heappush
from entities.graph import Edge, Graph
from ui.mock_gui import Mock_Gui


def dijkstra(graph: Graph, start, end=-1, GUI=Mock_Gui()):
    # -1 means inf. here, 0 index is never used (i hope!)
    handled = [False for i in range(graph.vertices + 1)]
    distances = [-1 for i in range(graph.vertices + 1)]
    distances[start] = 0  # pure extra
    heap = []
    heappush(heap, (0, start))
    round = 1
    while len(heap) > 0:
        dist, vertex = heappop(heap)
        if handled[vertex]:
            continue
        handled[vertex] = True
        dist_here = distances[vertex]
        for edge in graph.give_edges(vertex):
            # this is already be the shortest length.
            if not handled[edge.end]:
                dist_old = distances[edge.end]
                dist_new = dist_here + edge.weight
                if dist_old == -1 or dist_new < dist_old:
                    distances[edge.end] = dist_new
                    heappush(heap, (dist_new, edge.end))
        # For updating GUI for the visualization
        GUI.update_dijkstra(round, len(heap), handled, distances)
        round += 1
    return distances[end]
