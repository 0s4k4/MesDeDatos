##ejemplo de un diccionario

pokemons  = {
    'nombre': 'Bulbasaur',
    'NoPokedex': '1'
}

print(pokemons.get('nombre'));  ##mediante el metodo get se puedde acceder  aun elemento en especial del diccionario
print(pokemons['nombre']); ##se puede acceder tambien con corchetes como si fuera un arreglo

 
 ##actualizacion de valores de un diccionario
 
 ##mediante update

pokemons.update({
    'nombre': 'Squirtle',
    'NoPokedex': '4'
})

print(pokemons['nombre']+'\n'+pokemons['NoPokedex']);

##mediante corchetes
pokemons['nombre'] = 'Charmander';
pokemons['NoPokedex'] = '9';

print(pokemons['nombre']+'\n'+pokemons['NoPokedex'])

##adicion de elementos
pokemons['Tipo'] = 'Fuego';
print(pokemons['nombre']+'\n'+pokemons['NoPokedex']+'\n'+pokemons['Tipo'])

##se elimnan elementos
pokemons.pop('Tipo')
print(pokemons)

##datos complejos y diccionarios anidados


##se añaden los movimientos

pokemons['movimientos'] = {
    'Movimiento1':'Embestida',
    'Movimiento2':'Intimidar',
    'Movimiento3':'Vacio',
    'Movimiento4':'Vacio'
}

print(pokemons['movimientos'])  ##para acceder al diccionario añidado se solo es cuestion de referirlo el los corchetes



print('El pokemon '+pokemons['nombre'] +' tiene el numero '+pokemons['NoPokedex']+' y tiene el movimimiento ' + pokemons['movimientos']['Movimiento1'])
