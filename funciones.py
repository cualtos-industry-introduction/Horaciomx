lista = []
salida = "No"

def agregarContacto():
    nuevo_contacto = {}
    nuevo_contacto['nombre'] = input ("Ingresa el nombre del contracto: ")
    nuevo_contacto['correo'] = input ("Ingresa el correo del usario: ")
    nuevo_contacto['direccion'] = input ("Ingresa la direccion del usuario: ")
    lista.append(nuevo_contacto)

while(salida == "No"):
    entrada = input ("Escribe la acccion a efectuar: ")
    if entrada == "nuevo":
        agregarContacto()
        print("Contacto agregado")
    elif entrada == "mostrar":
        print(lista[:])
    elif entrada ==  "salir":
        exit()
    else:
        print("Opcoin no valida")
        