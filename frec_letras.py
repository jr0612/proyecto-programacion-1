import matplotlib.pyplot as plt
import unidecode 

def frec_letras(texto):
    
    texto = texto.lower()
    list(texto)
    d = {}
    for letra in texto:
        if not letra.isalpha():
            continue
        if letra == ' ':
            continue
        if letra == 'ñ':
            pass
        else:
            letra = unidecode.unidecode(letra)
        if letra not in d:
            d[letra] = 1
        else:
            d[letra] +=1
        
    llaves = d.keys()
    claves = d.values() 
    plt.bar(llaves, claves)
    plt.title("Frecuencia de letras en el texto")
    plt.xlabel("Letra")
    plt.ylabel("Frecuencia")
    plt.show()
