class Verkko:
    def __init__(self, solmuja, kaaret):
        """ 
        Luo verkon jossa (solmuja) solmua
        ja sanakirja Kaari:a avaimena kaaren alkupiste.
        Koska dict on niin paljon hitaampi kuin lista niin tää menee uusiks kokonaan
        """
        self.vertices = solmuja
        self.kaaret = {}
        for solmu in range(1, solmuja + 1):
            self.kaaret[solmu] = []
        for kaari in kaaret:
            self.kaaret[kaari.alku].append(kaari)

    def anna_kaaret(self, solmu):
        """
        Palauttaa listan kaaria joiden alkupiste on (solmu)
        """
        if solmu == 0:
            raise ValueError
            return []
        return self.kaaret[solmu]

    def give_edges(self, vertex):
        if vertex < 1 or vertex > self.vertices:
            raise ValueError
            return []
        return self.kaaret[vertex]


class Kaari:
    def __init__(self, alku, loppu, paino):
        """ 
        Kaari solmusta (alku) solmuun (loppu) jonka paino on (paino)
        """
        self.alku = alku
        self.loppu = loppu
        self.paino = paino
