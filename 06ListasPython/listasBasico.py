###para crear una lista se crea una variable y se introducen los valores dentro de [] 

planetas = ['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Urano','Neptuno']


##para acceder, se abre un arreglo, y se introduce la posicion, inicia desde 0
print(planetas[0]);
print('La cantidad de planetas en el sistema solar es de ' + str( len(planetas)));###len nos permite saber la longitud de una lista o coleccion


##podemos añadir mas elementos a la lista
planetas.append('Pluton');
print('anteriormente los planetas eran '  + str(len(planetas)));

##podemos eliminar un elemnto usando pop
planetas.pop()
print('Pero ahora los planetas son  ' + str(len(planetas)));

##mediante el uso de indices negativos podemos acceder al ultimo elemento usando -1 y al penultimo usando el -2


##usando index podemos buscar un elemento en nuestro lista 
tierra_index  = planetas.index('Tierra');
print('la tierra es el planeta numero ', str(tierra_index+1),'  del sistema solar');