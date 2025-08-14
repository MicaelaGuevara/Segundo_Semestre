# lista= Ariel, Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0:2])# Solo muestra el indice 0, 1 pero no el indice 2
# ir del indice de la lista al indice (sin incluirlo)
print(nombres[ :3])#Indice a mostrar
#Desde el indice indicado hasta el final
print(nombres[1: ]) 
#Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres:#nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene
print(len(nombres))# le pasamos como parametro la lista

#Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

#Insertar un elemento en un indice especifico 
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

#Eliminar un elemento
nombres.remove("Alberto")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice en especifico
del nombres[2] #del significado delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
print(nombres) #Aqui nos mostrara un error