def filtrar_nombres_que_empiezan_con(vocal, nombres):
    nombres_filtrados = []
 
    for nombre in nombres:
        if nombre[0] == vocal:
            nombres_filtrados.append(nombre)
    
    return nombres_filtrados
 
 
vocal = input("Ingrese una vocal: ")
if not vocal in ['A', 'E', 'I', 'O', 'U']:
    raise ValueError("Se ha ingresado un valor invalido, solo se aceptan vocales")
 
resultado = filtrar_nombres_que_empiezan_con(vocal, nombres)
print(resultado)