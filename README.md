#Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan 
# los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

from functools import reduce

elementos = ["amor", "roma", "arte", "trae", "esteban",  "juan", "nuevo",]


a = list(map(lambda palabra: ''.join(sorted(palabra)), elementos))


def palabras_parecidas(lista):
    palabras_unicas = []
    for palabra in lista:
        if palabra not in palabras_unicas and lista.count(palabra) > 1:
            palabras_unicas.append(palabra)
    return palabras_unicas


resultado = palabras_parecidas(a)


resultados_originales = []
for palabra in resultado:
    original = [elementos[i] for i in range(len(elementos)) if ''.join(sorted(elementos[i])) == palabra]
    resultados_originales.extend(original)


print(resultados_originales)
