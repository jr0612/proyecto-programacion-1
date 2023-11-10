preposiciones=set()
adverbios_lugar = {'cerca', 'lejos',  'entre', 'dentro', 'fuera', 'debajo', 'encima', 'sobre', 'detrás', 'delante', 'enfrente', 'frente', 'alrededor','alrededores','en','un','una','hacia'}
preposiciones2={'en','es','la' , 'un', 'una', 'a','su','mi', 'nuestra', 'de', 'y', 'pero', 'aunque'}

def nom_prop(texto):
    lista_texto = texto.split()
    lista_propia = {}
    for i in range(1,len(lista_texto)):
        pal = lista_texto[i]
        pal_ant = lista_texto[i-1]
        if pal.istitle() and not pal_ant.endswith(".") and not pal_ant.endswith("?") and not pal_ant.endswith(":") and not pal_ant.endswith("»") and len(pal)>2 and not pal.startswith("—"):
            lista_propia[lista_texto[i]] = i
    return lista_propia


def lugares(lista_propia, texto ):
    lugares = set()
    nombres = set()
    palabras = texto.lower().split()
    for key in lista_propia.keys():
        if (quitar_simbolos_no_alpha(palabras[lista_propia[key]-1]) in preposiciones or adverbios_lugar) or (quitar_simbolos_no_alpha(palabras[lista_propia[key]-2]) in preposiciones or adverbios_lugar):
            if palabras[lista_propia[key]] not in preposiciones2 or palabras[lista_propia[key]] not in adverbios_lugar:
                lugares.add(quitar_simbolos_no_alpha(key))
    
    return lugares
    
    


def frec_personajes(personajes, texto):
    palabras = texto.split()
    frec={}
    frec_final={}
    for palabra in palabras:
        if palabra in personajes:
            f= frec.get(palabra, 0)
            frec[palabra] = f+1
    
    
    for key in frec.keys():
        f = frec.get(key)
        key = quitar_simbolos_no_alpha(key)
        if key not in frec_final:
            frec_final[key] = f
        else:
            frec_final[key] += f

    return frec_final
    



def quitar_simbolos_no_alpha(pal):
    while not pal[-1].isalpha():
        if len(pal) ==1 : return ''
        else:
            pal = pal[:-1]
    return pal







