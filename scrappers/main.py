from lib import get_brands_ids, get_brands_name, get_materials, get_sizes
import string



def print_texts(textos):
    for texto in textos:
        print(texto)

if(__name__=="__main__"):
    letters = string.ascii_uppercase

    for letter in letters:
        
        if letter == 'Q':
            print('Quechua\nQuiksilver\nQuiz')
            continue
        if letter == 'X':
            print('Xbox')
            continue
        
        archivo_html = letter+ '_elements.html'  # Reemplaza con la ruta de tu archivo HTML
        textos = get_brands_name.extraer_textos(archivo_html)
        print_texts(textos)
    
    get_brands_ids.exec("nombres_marcas.txt")
