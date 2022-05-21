import requests


def httpcall(osoite: str, *args):
    # payload = {key1:value1, key2:value2}
    r = requests.get(osoite)  # , params=payload)
    print(r.url)
    return r.text  # palauttaa nyt kaiken
