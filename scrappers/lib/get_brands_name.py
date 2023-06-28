from bs4 import BeautifulSoup

def camel_case(texto):
    palabras = texto.split()
    capitalizado = [palabra.capitalize() for palabra in palabras]
    return "".join(capitalizado)

def extraer_textos(html_file):
    with open(html_file, 'r') as file:
        text_html = file.read()
        
    soup = BeautifulSoup(text_html, 'html.parser')
    
    divs = soup.find_all('div', class_='follow__header')
    
    textos_etiqueta_a = []
    for div in divs:
        etiqueta_a = div.find('a')
        if etiqueta_a is not None:
            texto = etiqueta_a.get_text(strip=True)
            texto_camel_case = camel_case(texto)
            textos_etiqueta_a.append(texto_camel_case)
    return textos_etiqueta_a

