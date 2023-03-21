lunas_de_planetas = {
    
    'mercurio':0,
    'venus':0,
    'tierra':1,
    'marte':2,
    'jupiter':79,
    'saturno':82,
    'urano':27,
    'neptuno':14,
    'pluton':5,
    'makemake':1,
    'eris':1 
}

lunas = lunas_de_planetas.values() ##con values podemos obtener el valor de los diccionarios

total_lunas = len(lunas_de_planetas.keys())
print(total_lunas);