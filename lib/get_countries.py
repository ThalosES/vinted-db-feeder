import requests
import time

from lib import get_brands_names

class Country:
    def __init__(self, id, title, local, iso_code):
        self.id = id
        self.title = title
        self.local= local
        self.iso_code = iso_code


def get_data(url: str, sess: requests.Session):
    response = sess.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def deserialize_json(data) -> list[Country]:
    countries = []
    for country in data["countries"]:
        d_country = Country(
            id=country["id"],
            title=country["title"],
            local=country["title_local"],
            iso_code=country["iso_code"]
        )
        countries.append(d_country)

    return countries

def exec(outfilename):
    pass

    outfile= open(outfilename, "w")
    outfile.truncate()
    outfile.write("ID, COUNTRY, LOCAL, ISO\n")
    
    res=""

    URL = "https://www.vinted.es/api/v2/countries"

    URL_COOKIES = 'https://www.vinted.es/auth/token_refresh'

    sess = requests.Session()
    
    HEADERS = {
                "User-Agent": "PostmanRuntime/7.28.4",  # random.choice(USER_AGENTS),
                "Host": "www.vinted.es",
    }

    sess.headers.update(HEADERS)

    sess.post(URL_COOKIES)

    # Obtener los datos
    data = get_data(URL, sess)

    if data is not None:
        # Serializar el JSON
        deserialized_data = deserialize_json(data)
        # Imprimir los resultados deserializados
        if len(deserialized_data) > 0:
            for country in deserialized_data:
                res+=(f"{country.id} , \'{country.title}\' , \'{country.local}\', \'{country.iso_code}\'\n")
                print(country.title+ " ✔️")
    else:
        print("Error al obtener los datos.")

    outfile.write(res)
    outfile.close()