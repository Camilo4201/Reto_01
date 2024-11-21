#Escribir una función que reciba una lista de números enteros 
# y retorne la mayor suma entre dos elementos consecutivos.
def Mayor_Suma(lista):
    if len(lista) < 2:
        return None
    return max(a + b for a, b in zip(lista, lista[1:]))

entrada = input("Ingrese la lista de números (separados por espacios): ")
lista = list(map(int, entrada.split()))
resultado = Mayor_Suma(lista)
print(f"La mayor suma entre dos elementos consecutivos es: {resultado}")
