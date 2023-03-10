###las listas tambien se pueden trabajar con numeros


gravedad_planetas =  [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

pesoBus_tierra = 1260;

print('En la tierra un bus pesa' , int(pesoBus_tierra))
print('El peso de un bus en mercurio es de ',str(pesoBus_tierra*gravedad_planetas[0]));


##con las funciones min and max podemos devolver los valores mas grandes de un arreglo

print("el peso mayor de un bus en los planetas del sistema solar es de ", pesoBus_tierra * max(gravedad_planetas), "kg")
print('El peso menor de un bus en el sistema solar es de', pesoBus_tierra * min(gravedad_planetas),'KG' )