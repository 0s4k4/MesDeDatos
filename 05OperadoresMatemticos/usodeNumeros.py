###convertir cadenas en numero}

numer1 = int(input('Ingresa el numero 1 '));
##mediante las funciones int y float se puede convertir un numero cadena  a uno de numero.
##print(type(numer1));

numero1 = 39;
numero2 = 16;

op1 = 39-16
op2 = 16-39

print(abs(op1))
print(abs(op2))


##mediante abs nos permite obtener un resultado absoluto sin negativos

calificacion = float(input('inserta tu calificacion'));
print('Tu calificacion es de: '+ str(round(calificacion)));  
##mediante la funcion round podemos redondear el numero o cantidad, con STR concatenamos nuestro dato  a string para combinarlo con la cadena de texto y poder imprimir el mensaje en el print