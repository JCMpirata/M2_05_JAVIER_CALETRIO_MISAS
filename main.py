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

#Ejercicio 3
frase = input("Introduce tu texto: ")
contador = 0
for letra in frase:
  if letra == "a":
    contador = contador + 1
print(f"En el texto aparecen {contador} letras a")

#Ejercicio 2
numeros = ["26", "15", "32"]
if numeros:
  A = numeros.sort()
  print("Estan en orden ascendente")
else:
  print("No estan en orden ascendente")

#Ejercicio 1
def pedirNumero():
  while True:
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce un numero: "))
    num3 = int(input("Introduce un numero: "))
    if num1<num2<num3 != 0:
    print(True)







