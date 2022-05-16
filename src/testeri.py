from entities.Verkko import Kaari, Verkko
from djikstra import djikstra
from ui.mock_gui import Mock_Gui

# tehdään ensin 5 solmuinen verkko, jossa kaikkien pisteiden välillä kaari
# tirakirjan kuvan 11.4 verkko
VERKKO1 = Verkko(5, [
    Kaari(1, 2, 8),
    Kaari(1, 3, 2),
    Kaari(2, 4, 5),
    Kaari(3, 2, 4),
    Kaari(3, 5, 7),
    Kaari(5, 4, 3),
])
mok = Mock_Gui()
djikstra(verkko=VERKKO1, alku=1, GUI=mok)
