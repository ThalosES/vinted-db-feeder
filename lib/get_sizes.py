from typing import List
from bs4 import BeautifulSoup, PageElement
import re, os

category_to_id = {
    "HOGAR":"1918",
    "HOMBRE":"5",
    "MASCOTAS":"2093",
    "MUJER":"1904",
    "NIÑOS":"1193"
}

class Size:
    def __init__(self, id, title, size_type):
        self.id = id
        self.title = title
        self.category = size_type
    
    def __str__(self):
        return f"{self.id}, '{self.title}', '{self.category}'"


def obtener(path):

    with open(path, 'r') as file:
        contenido_html = file.read()
    
    soup = BeautifulSoup(contenido_html, 'html.parser')

    p = file.name.split('/')
    category_name= p[len(p)-1].split('.')[0].upper()
    category_id = category_to_id[category_name]

    pile_elements:List[PageElement] = soup.find_all('li', class_='pile__element')

    # Initialize a list to store the size objects
    sizes_list:List[Size] = list()

    # Iterate through the pile__element elements
    for element in pile_elements:
        
        # Get ID
        pile_element_div = element.find('div', class_='web_ui__Cell__cell web_ui__Cell__default web_ui__Cell__navigating')
        pile_element_id = pile_element_div.get('id')
        id_parts = pile_element_id.split('-')
        id = id_parts[-1]

        # Get size name
        size_name = element.find('h2', class_='web_ui__Text__text web_ui__Text__title web_ui__Text__left').text.strip()

        # Get category
        pile = element.parent.fetchPreviousSiblings()[0]

        # Extract the category from the h3 tag
        size_type = pile.find('h3', class_='web_ui__Text__text web_ui__Text__subtitle web_ui__Text__left').text.strip()

        size_obj = Size(id, size_name, size_type)

        sizes_list.append(size_obj)

    # Agregar las etiquetas encontradas a la lista

    return (sizes_list, category_id)

def print_result(lista, category_name) -> str:
    result=""
    for size in lista:
        result+=f"{size}, {category_name}\n"
    return result

def exec(path, outfilename):

    outfile= open(outfilename, "w")
    outfile.truncate()
    outfile.write("ID, SIZE, SIZE_TYPE_ES, CATEGORY_ID\n")

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            lista, cat = obtener(file_path)
            outfile.write(print_result(lista, cat))
    outfile.close()
