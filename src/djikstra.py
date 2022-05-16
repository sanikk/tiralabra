from heapq import heappop, heappush
# varmaan tarpeeton, ei tän tartte noita ymmärtää, kunhan käyttää
from entities.Verkko import Kaari, Verkko
from ui.mock_gui import Mock_Gui


def djikstra(verkko: Verkko, alku, loppu=-1, GUI=Mock_Gui()):
    kasitelty = [False for i in range(verkko.solmuja + 1)]
    kasitelty[0] = True  # hupia =) tätä ei ikinä käsitellä muutenkaan
    etaisyys = [-1 for i in range(verkko.solmuja + 1)]
    etaisyys[0] = 0  # hupia, tätä ei ikinä käsitellä
    etaisyys[alku] = 0
    keko = []
    heappush(keko, (0, alku))
    kierros = 1
    while len(keko) > 0:
        matka, solmu = heappop(keko)
        if kasitelty[solmu]:
            continue
        kasitelty[solmu] = True
        for kaari in verkko.anna_kaaret(solmu):
            if not kasitelty[kaari.loppu]:
                nyky = etaisyys[kaari.loppu]
                uusi = etaisyys[solmu] + kaari.paino
                if nyky == -1 or uusi < nyky:
                    etaisyys[kaari.loppu] = uusi
                    heappush(keko, (uusi, kaari.loppu))
        GUI.update_gui(kierros, len(keko), kasitelty, etaisyys)
        kierros += 1
    return etaisyys[loppu]
