##Ejercicio: Usa lógica compleja para determinar posibles maniobras evasivas
##En el ejercicio anterior, creó código para probar el tamaño del objeto. Ahora probará tanto el tamaño como la proximidad del objeto. Utilizará el mismo umbral para un tamaño de 5 m3. Si el objeto es más grande que el umbral y se encuentra dentro de los 1000 km del barco, se requerirán maniobras evasivas.
##Para este paso, se le presentará el objetivo del ejercicio, seguido de una celda vacía. Ingrese su Python en la celda y ejecútelo. La solución está al final del ejercicio.
##Agregue el código a la celda a continuación para crear dos variables: object_size y proximidad. Establezca object_size en 10 para representar 10m3. Establecer la proximidad a 9000.
##A continuación, agregue el código para mostrar un mensaje que indique que se requieren maniobras evasivas si el tamaño del objeto es mayor que 5 y la proximidad es menor que 1000. De lo contrario, muestre un mensaje que diga que el objeto no representa una amenaza.


tamañoDeObjeto = 10;
proximidad = 9000;


if tamañoDeObjeto > 5  and proximidad < 10000:
    print('requieren maniobras evasivas')
else :
    print('No se requieren maniobras evasivas');
