def contar_palabras_diferentes(texto):
    palabras = texto.split()  
    palabras_diferentes = set(palabras)  
    cantidad_palabras_diferentes = len(palabras_diferentes)  
    return cantidad_palabras_diferentes 
