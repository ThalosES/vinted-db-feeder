from bs4 import BeautifulSoup
import re, os

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
    res=""
    for num , texto in textos:
        res+=(str(num) + ', \'' +texto+"\'\n")
    return res

def exec(folder, outfolder):
    
    if(os.path.exists(outfolder)==False):
        os.mkdir(outfolder)

    for filename in os.listdir(folder):
        file_name = filename.split(".")[0]+".csv"
        html_file = os.path.join(folder, filename)
        if os.path.isfile(html_file):
            outfile= open(outfolder+file_name, "w")
            outfile.truncate()
            outfile.write("ID, MATERIAL\n")
            textos = extraer_textos(html_file)
            outfile.write(print_texts(textos))
            outfile.close()
