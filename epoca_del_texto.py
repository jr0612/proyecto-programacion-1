import re

def determinar_periodo_tiempo(texto):
    patron_fecha = r'\b\d{4}\b'

    fechas_encontradas = re.findall(patron_fecha, texto)

    if fechas_encontradas:
        años = [int(año) for año in fechas_encontradas]
        año_promedio = sum(años) // len(años)
        
        if año_promedio >= 1800 and año_promedio <= 2022:
            return f"La obra transcurre durante la Edad Contemporánea, aproximadamente alrededor del año {año_promedio}."
        elif año_promedio > 2022:
            return f"La obra es futurista, con una fecha promedio aproximada alrededor del año {año_promedio}."
        else:
            return f"La obra es anterior a la Edad Contemporánea, aproximadamente alrededor del año {año_promedio}."

    else:
        
        palabras_clave = ["industria", "tecnología", "computadora","celular", "internet","carro","automovil"]

        if any(palabra in texto for palabra in palabras_clave):
            return "La obra transcurre durante la Edad Contemporánea"
        else:
            return "La obra es anterior a la Edad Contemporánea"

