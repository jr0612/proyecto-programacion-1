def invertir_diccionario_duplicados(dicc):
    inv = {}
    for llave, valor in dicc.items():
        lista = inv.get(valor, [])
        lista.append(llave)
        inv[valor] = lista
    return inv
def frec_palabras(texto):
    
    lista_texto = texto.split()
    pal_100 = []
    frecu = {}
    for pal in lista_texto:
        pal = pal.replace(':','')
        pal = pal.replace('.','')
        pal = pal.replace('?','')
        pal = pal.replace('¿','')
        pal = pal.replace('-','')
        pal = pal.replace(',','')
        pal = pal.replace(';','')

        if not pal.isalpha():
            continue
        if pal not in frecu:
            frecu[pal] = 1
        else:
            frecu[pal] += 1
    inv = invertir_diccionario_duplicados(frecu)
    vals = list(inv.keys())
    vals.sort(reverse=True)
    dic_ord = {}
    for num in vals:
        dic_ord[num] = inv[num]
     

    for i in dic_ord:
        palabras = dic_ord[i]
        if len(pal_100) >= 100:
            break
        if len(palabras)>=100:
            for r in range(0,100):
                if len(pal_100) >= 100:
                    break
                pal_100.append(palabras[r])
        else:
             for q in range(len(palabras)):
                if len(pal_100) >=100:
                    break
                pal_100.append(palabras[q])
    return pal_100

