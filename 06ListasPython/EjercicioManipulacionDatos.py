planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]


planetaDelUsuario =  input('Introduce el planeta del usuario')

planetaIndex = planets.index(planetaDelUsuario)

print('El planeta en el que estas es el  numero ',planetaIndex+1,'   del sistema solar ')