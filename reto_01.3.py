#Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. 
# La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
Lista = range(20)
Lista_Numeros_Primos=[x for x in Lista if x>1 and all(x%i !=0 for i in range(2,int(x**0.5)+1))] 
print(list(Lista_Numeros_Primos))
  
