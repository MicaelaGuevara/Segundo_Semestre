#Crear una  lista que solo incluya los numeros menores a 5
#Imprimir por consola [1, 3, 2]


#Definimos la tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

lista_menores = [num for num in tupla if num < 5]

print(lista_menores)