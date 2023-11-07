import matplotlib.pyplot as plt

def histograma_longitudes_palabras(texto):
    palabras = texto.split()
    longitudPalabras = {}  
    
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in longitudPalabras:
            longitudPalabras[longitud] += 1
        else:
            longitudPalabras[longitud] = 1
    plt.bar(longitudPalabras.keys(), longitudPalabras.values())
    plt.xlabel('Longitud de Palabra')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Longitudes de Palabras')
    plt.show()
