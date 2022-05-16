class Verkko:
    def __init__(self, solmuja, kaaret):
        """ 
        Luo verkon jossa (solmuja) solmua
        ja sanakirja Kaari:a avaimena kaaren alkupiste.
        """
        self.solmuja = solmuja
        self.kaaret = {}
        for solmu in range(1, solmuja + 1):
            self.kaaret[solmu] = []
        for kaari in kaaret:
            self.kaaret[kaari.alku].append(kaari)

    def anna_kaaret(self, solmu):
        """
        Palauttaa listan kaaria joiden alkupiste on (solmu)
        """
        return self.kaaret[solmu]


class Kaari:
    def __init__(self, alku, loppu, paino):
        """ 
        Kaari solmusta (alku) solmuun (loppu) jonka paino on (paino)
        """
        self.alku = alku
        self.loppu = loppu
        self.paino = paino
