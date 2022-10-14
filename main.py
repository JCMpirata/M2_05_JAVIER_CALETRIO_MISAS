#Ejercicio 4
paises = ["España", "Alemania", "Francia", "Suiza", "Dinamarca"]
print(paises)
#Elementos y longitud de los elementos de la lista
print(paises[0], len(paises[0]))
print(paises[1], len(paises[1]))
print(paises[2], len(paises[2]))
print(paises[3], len(paises[3]))
print(paises[4], len(paises[4]))
#Elemento con mayor numero de caracteres
print(f"El elemento con mas caracteres es: ", paises[4])
#Palabras ordenadas de menor a mayor longitud
paises.sort(key=len)
print(paises)
#Palabras ordenadas de mayor a menor longitud
paises.sort(key=len, reverse = True)
print(paises)

print("\n")

#Ejercicio 3
frase = input("Introduce tu texto: ")
contador = 0
for letra in frase:
  if letra == "a":
    contador = contador + 1
print(f"En el texto aparecen {contador} letras a")


print("\n")

#Ejercicio 2
numeros = list()
A = numeros.append(input("Añade un numero: "))
A = numeros.append(input("Añade un numero: "))
A = numeros.append(input("Añade un numero: "))
if numeros[0] == 0:
  print("Error")
elif numeros[0]<numeros[1]<numeros[2]:  
  print("Estan en orden ascendente")
else:
  print("No estan en orden ascendente")
      
print("\n")

#Ejercicio 1
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
if num1 == 0:
  print("Error")
elif num1<num2<num3:
  print("Estan en orden ascendente")
else:
  print("No estan en orden ascendente")
    








