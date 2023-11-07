def contar_caracteres(text):
    contador = 0
    for simbolo in text:
        contador += 1
 
    return contador

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)
