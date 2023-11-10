import spacy
import lugares_y_nombres
e = spacy.load("es_core_news_md")
def lugares_libreria(texto, punto):
    lug = []
    nom = []
    texto = lugares_y_nombres.nom_prop(texto)
    for place in texto:
        d = e(place)
        lugarcito = []
        for i in d.ents:
            if i.label_ == "LOC":
                lugarcito.append(i.text)
            if lugarcito:
                lug.append(lugarcito)
            else:
                nom.append(place)

    if punto == 'lugares':
        return lug
    elif punto =='personajes':
        return nom
    

