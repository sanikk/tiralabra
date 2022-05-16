from entities.Verkko import Kaari, Verkko
from djikstra_with_extras import djikstra
from ui.mock_gui import Mock_Gui
from entities.Graph import Edge, Graph

# tehdään ensin 5 solmuinen verkko, jossa kaikkien pisteiden välillä kaari
# tirakirjan kuvan 11.4 verkko
VERKKO0 = Verkko(5, [
    Kaari(1, 2, 8),
    Kaari(1, 3, 2),
    Kaari(2, 4, 5),
    Kaari(3, 2, 4),
    Kaari(3, 5, 7),
    Kaari(5, 4, 3),
])
VERKKO1 = Graph(5, [
    Edge(1, 2, 8),
    Edge(1, 3, 2),
    Edge(2, 4, 5),
    Edge(3, 2, 4),
    Edge(3, 5, 7),
    Edge(5, 4, 3),
])
mok = Mock_Gui()
#djikstra(graph=VERKKO1, start=1, GUI=mok)
djikstra(graph=VERKKO1, start=1, end=5, GUI=mok)
