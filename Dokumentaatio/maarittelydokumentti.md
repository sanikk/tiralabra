# DIA* ja Dijkstra vertailu 
Tarkoituksena tehdä IDA* ja Dijkstra vertailu, eli molempien käytännön toteutuksista liikkeelle ja openmapdatalla. Tutustun varmaan sivussa hsl apiin,
mutta fokus lienee etäisyyksissä ilman matka-ajoilla painotettuja kaaria.

Harjoitustyö on osa Tkt-opintoja, teen tämän Pythonilla Javan sijaan, mutta vertaisarvioinnit käyvät sekä Javalla että Pythonilla. Kielenä suomi ainakin 
tämän viikkopalautuksen ajan. 

Dijkstralle tämä aikavaativuus on ilmeisesti O(n + m log m), missä m log m on keon toiminnasta johtuvaa. Ainakaan alustavassa versiossa käyttämäni valmiin prioriteettijonon eli heapq:n toteutuksesta (https://github.com/python/cpython/blob/3.10/Lib/heapq.py) en heti huomaa mitään syytä miksi tämän pitäisi olla oleellisesti hitaampi. Toivottavasti pääsen omalla kyhäelmälläni suunnilleen samaan. 

IDA*n aikavaativuus riippuu ilmeisesti suurelta osalta heuristiikkafunktion soveltuvuudesta.

Molempien algoritmien toteutuksessa on pyritty seuraamaan hyviä käytänteitä Pythonilla, tosin aiheesta johtuen teho menee tarvittaessa luettavuuden edelle, mutta pyrin huomioimaan tämän kommenteissa. Ilmeisiä optimisaatioita on tehty jonkun verran, mutta myös melko naiviit versiot on tallennettu toimivina, ja testattuina.

Lähteet: (pseudot + aika- ja tilavaatimukset) 
https://en.m.wikipedia.org/wiki/Dijkstra%27s_algorithm
https://en.m.wikipedia.org/wiki/Iterative_deepening_A*
tirakirja (A.Laaksonen) fetched from [redacted] on ?.?.????
https://doi.org/10.1016/S0004-3702(01)00094-7 Korf, R., Reid, M., Edelkamp, S. Time complexity of iterative-deepening-A*

toteutuksesta pythonissa:
https://wiki.python.org/moin/TimeComplexity (lista-operaatiot vs muiden tietorakenteiden operaatiot)
https://github.com/python/cpython/blob/3.10/Lib/heapq.py (heapq-keko)
https://wiki.python.org/moin/PythonSpeed/PerformanceTips

