#Crear una función que realice operaciones básicas (suma, resta, multiplicación, división)
#  entre dos números, según la elección del usuario, la forma de entrada de la función será    
# los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
def calculadora(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    if operacion == "-":
        return numero1 - numero2
    if operacion == "*":
        return numero1 * numero2
    if operacion == "/":
        if numero2 != 0:  
            return numero1 / numero2
        else:
            
            return "Error: Division por cero no permitida."
    else:
        return "Una operacion invalida"


numero1 = float(input("Ingrese el primer numero:"))
numero2 = float(input("Ingrese el segundo numero:"))
operacion = input("Ingrese la operacion a realizar:")


resultado = calculadora(numero1, numero2, operacion)
print("El resultado es:", resultado)


