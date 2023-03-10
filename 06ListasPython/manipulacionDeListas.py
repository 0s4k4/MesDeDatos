planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
##podemos segmentar la lista usando corchetes
planetas_antesDeTierra = planets[0:2]
print('Los planetas antes de la tierra son ' , planetas_antesDeTierra)
##si no ponemos un fin en el rango del corchete de la segmentacion, va a leer todo el arreglo hasta el ultimo elemento

###combinacion de listas
PokemonsInicialesKanto = ['Bulbasaur','Squirtle','Charmander']
PokemonsInicialesJhoto = ['Chikorita','Totodile','Cindaquil']

print('Los pokemons iniciales de las primeras ediciones son :', PokemonsInicialesKanto +  PokemonsInicialesJhoto )

###para ordenar nuestras listas del mayor y menor se usa el sort

PokemonsInicialesJhoto.sort()
print('El orden alfabetico de nuestros iniciales es ',PokemonsInicialesJhoto)

##si queremos hacerlo inverso asi es
PokemonsInicialesKanto.sort(reverse=True)
print('El orden de los pokemons de manera alfabetica inversa es ',PokemonsInicialesKanto)

##sort nos modifica la lista actual a un orden segun el argumento que se le pase dentro de la funcion
