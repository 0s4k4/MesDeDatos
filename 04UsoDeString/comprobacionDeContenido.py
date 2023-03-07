


temperaturas = 'En reynosa la temperatura es de: 40 C'
partes = temperaturas.split(':');
##print(partes[-1]);

##el metodo de split nos permite separar apartir de un caracter  y con la posicion de partes[-1] nos devuelve la ultima posicion del arreglo

temperaturaEnInvierto = 'La temperatura promedio en invierno fue de menos 18 grados en reynosa'

for item in temperaturaEnInvierto.split():
    if item.isnumeric():
         print()
##CON EL METODO is numeric, nos ayud a buscar caracteres numericos en nuesta cadena de text

###para valores negativos o con caracter, se usa el end and startswitch

temperaturaMasBaja = '-18'

if temperaturaEnInvierto.startswith('-'):
    print('la temperatura ha sido bajo cero')

##transformacion de texto

texto = 'Hola, la password es 123, recuerdala'.replace('123','****')
print(texto)
