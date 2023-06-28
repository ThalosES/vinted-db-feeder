import requests
import time

from lib import get_brands_names

class Color:
    def __init__(self, id, title, hex):
        self.id = id
        self.title = title
        self.hex = hex


def get_data(url, sess):
    response = sess.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def deserialize_json(data):
    colors = []
    for color in data["brands"]:
        d_color = Color(
            id=color["id"],
            title=color["title"],
            hex=color["hex"]
        )
        colors.append(d_color)

    return colors

def exec(brand_name_file, outfilename):

    brand_names= get_brands_names.exec(brand_name_file)

    outfile= open(outfilename, "r+")
    outfile.truncate()
    outfile.write("ID, TITLE, URL\n")
    
    res=""

    base_url = "https://www.vinted.es/api/v2/brands?keyword="

    url_cookies = 'https://www.vinted.es/auth/token_refresh'

    sess = requests.Session()
    
    HEADERS = {
                "User-Agent": "PostmanRuntime/7.28.4",  # random.choice(USER_AGENTS),
                "Host": "www.vinted.es",
    }

    sess.headers.update(HEADERS)

    sess.post(url_cookies)
    for brand in brand_names:
    
        url = base_url+brand

        # Obtener los datos
        data = get_data(url, sess)

        if data is not None:
            # Serializar el JSON
            deserialized_data = deserialize_json(data)
            # Imprimir los resultados deserializados
            if len(deserialized_data.brands) > 0:
                brand = deserialized_data.brands[0]
                res+=(f"{brand.id} , {brand.title} , {brand.url}\n")
                print(brand.title+ " ✔️")
        else:
            print("Error al obtener los datos.")

        #time.sleep(0.1)

    outfile.write(res)
    outfile.close()