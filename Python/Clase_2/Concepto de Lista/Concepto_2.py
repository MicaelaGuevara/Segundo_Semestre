#Concatectemos Listas

lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 #Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) #Funcion para agregar varios eleentos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para ublicar en un indice esta el valor ingresado
#print(lista3.index(0)) #Esto daria un error por no ser el elemento parte de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al revez una lista
lista3.reverse()
print(lista3)