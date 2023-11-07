def detectar_idioma_2(texto):
    patrones_idiomas = {"español": "aeiouáéíóúüñ", "ingles": "aeiouy", "frances": "aeiouàâéèêëîïôùûüÿ", "aleman": "aeiouäöüß","portugues": "aeiouáâãàéêíóôõúü"
    }
    letras = ''.join(filter(str.isalpha, texto.lower()))
    frecuencias = {}
    for idioma, patrones in patrones_idiomas.items():
        frecuencias[idioma] = sum(letra in patrones for letra in letras)
    idioma_detectado = max(frecuencias, key=frecuencias.get)
    
    return idioma_detectado
