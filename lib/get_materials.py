from bs4 import BeautifulSoup
import re

def extraer_textos(html_file):
    with open(html_file, 'r') as file:
        text_html = file.read()
        
    soup = BeautifulSoup(text_html, 'html.parser')
    pattern = re.compile(r'material_ids-list-item-(\d+)')
    
    divs = soup.find_all('div', attrs={'id' : pattern})
    
    textos_etiqueta_a = []
    for div in divs:
        match = re.match(pattern, div['id'])
        if match:
            valor_h2 = div.find('h2').text
            numero = match.group(1)
            textos_etiqueta_a.append((numero , valor_h2))
    return textos_etiqueta_a

def print_texts(textos):
    for num , texto in textos:
        print(str(num) + ', ' +texto)

def exec(html_file):
    textos = extraer_textos(html_file)
    print_texts(textos)
