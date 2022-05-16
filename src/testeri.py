from djikstra_with_extras import djikstra
from ui.mock_gui import Mock_Gui
from entities.Graph import Edge, Graph

# first a graph with 5 vertices, source tirakirja pic 11.4

VERKKO1 = Graph(5, [
    Edge(1, 2, 8),
    Edge(1, 3, 2),
    Edge(2, 4, 5),
    Edge(3, 2, 4),
    Edge(3, 5, 7),
    Edge(5, 4, 3),
])

# mock_gui so just the prints

mok = Mock_Gui()

# various test inputs

#djikstra(graph=VERKKO1, start=1, GUI=mok)
djikstra(graph=VERKKO1, start=1, end=5, GUI=mok)
