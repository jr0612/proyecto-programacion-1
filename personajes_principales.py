def personajes_principales(frec_personajes):
    personajes_principales = []
    frec_personajes = invertir_diccionario(frec_personajes)
    frecuencias = list(frec_personajes.keys())
    frecuencias.sort(reverse=True)
    
    for key in frecuencias:
        personajes_principales.append(frec_personajes[key])
    personajes_principales = personajes_principales[:3]

    return personajes_principales
        




def invertir_diccionario(dicc):
    inv = {}
    for llave, valor in dicc.items():
        lista = inv.get(valor, [])
        lista.append(llave)
        inv[valor] = lista
    return inv


