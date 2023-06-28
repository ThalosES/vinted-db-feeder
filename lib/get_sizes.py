from bs4 import BeautifulSoup
import re, os

def obtener(path):
    numeros = []

    with open(path, 'r') as file:
        contenido_html = file.read()

    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'html.parser')
    div = soup.find_all('div', attrs={'class': 'web_ui__Navigation__body'})
    categoria = div[0].text
    pattern = re.compile(r'size_group_sizes_(\d+)-list-item-(\d+)')
        
    # Encontrar todas las etiquetas label con el atributo for igual a 'size_group_sizes_4_'
    divs = soup.find_all('div', attrs={'id': pattern})
    
    for div in divs:
        match = re.match(pattern, div['id'])
        if match:
            valor_h2 = div.find('h2').text
            numero = match.group(2)
            numeros.append((numero , valor_h2))
    # Agregar las etiquetas encontradas a la lista

    return (numeros , categoria)

def print_result(lista , categoria):
    res=""
    for num, val in lista:
        res+=(num + " , " + val + " , "+ categoria+"\n")
    return res

def exec(path, outfilename):

    outfile= open(outfilename, "w")
    outfile.truncate()
    outfile.write("ID, SIZE, CATEGORY\n")

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            numeros , categoria = obtener(file_path)
            outfile.write(print_result(numeros , categoria))
    outfile.close()
