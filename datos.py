tupla = 1, 2, 3, 4, 'Hola', 3.2
print(tupla[:])
#tupla[0] = 3
diccionario ={'nombre': 'Juan', 'apellido': 'Lopez'}
usuario = {'nombre': 'Pedro', 'apellido': 'sanchez'}
lista = [diccionario, usuario]
print(diccionario['nombre'])
print(lista[1:2])
for registro in lista:
    print(registro)


usuario['correo'] = "abc@correo.com"

#for registro 

datos ={}
datos['nombre'] = input("ingresa en uno nombre:")
datos['direccion'] = input("ingresa la direccion:")
datos['correo'] = input("ingresa en correo:")

print(lista[0]['nombre'])
for llave, valor in usuario.items():
    print(llave, valor)

lista.append(datos)
