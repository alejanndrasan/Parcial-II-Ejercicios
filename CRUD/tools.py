'''Aplicando el método CRUD, crea un programa que maneje la base de datos de trabajadores de una tienda. Debe tener las opciones de:
Registrar persona
Modificar persona
Ver personas
Eliminar persona'''

from Persona import Persona

def cargar_datos(txt, db):
    with open(txt) as dbe:
        db = dbe.readlines()
    return db

#Validaciones:

def val_str(msg1, msg2):
    while True:
        string = input(msg1)
        if string.replace(" ", "").isalpha():
            string = string.title()
            return string
            break
        else:
            print(msg2)

def val_int(msg1, msg2, n):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num)<n:
            num = int(num)
            return num
            break
        else:
            print(msg2)

#Funciones:

def mostrar_cargos(): 
    cargos = [("Gerente",10000),("Vendedor",6000),("Encargado de almacén",5500),("Personal de mantenimiento",2000)]
    for i, c in enumerate(cargos):
        print(f'''{i+1}. {c[0]}.''')

def definir_cargo(m):
    cargos = [("Gerente",10000),("Vendedor",6000),("Encargado de almacén",5500),("Personal de mantenimiento",2000)]
    cargo = cargos[m][0]
    return cargo

def definir_sueldo(m):
    cargos = [("Gerente",10000),("Vendedor",6000),("Encargado de almacén",5500),("Personal de mantenimiento",2000)]
    sueldo = cargos[m][1]
    return sueldo

def registrar_empleado(nombre):
    edad = val_int('\nInserte la edad del empleado:  ', "\nEdad no valida, vuelva a intentar", 100)

    while True:
        genero = val_str('\nIngrese su genero (F, M u O):  ', '\nNo valido, intente otra vez')
        if genero == 'F' or genero == 'M' or genero=='O':
            break
        else:
            print('\nIntente otra vez')

    cedula = val_int('\nIngrese su numero de cedula sin caracteres especiales: ', '\nNo valido, intente otra vez', 1000000000)
    mostrar_cargos()
    i_cargo = val_int('\nSeleccione una de las opciones:  ', "\nOpcion no valida, intente otra vez", 5 )
    cargo = definir_cargo(i_cargo)
    sueldo = definir_sueldo(i_cargo)

    empleado_n = Persona(nombre, edad, genero, cedula, cargo, sueldo)

    with open("C:\\Users\\Jsantos\Desktop\\CLASES ALGORITMOS\\Parcial II practicas\\CRUD\\registro_empleados.txt","a+") as dbe:
        dbe.write(f"{empleado_n.nombre}//{edad}//{genero}//{cedula}//{cargo}//{sueldo}\n")

    print("\nEmpleado registrado con éxito.")
    
    return empleado_n

def cosificacion_empleados(lista, lista2):
    lista2=[]
    for i in range(len(lista)):
        empleado = lista[i].split('//')
        empleado_n = Persona(empleado[0],empleado[1],empleado[2],empleado[3],empleado[4],empleado[5])
        lista2.append(empleado_n)
    return lista2
    

def verificar_empleado(lista):
    temp = False
    nombre = val_str("\nInserte el nombre completo del empleado: ", '\nNombre invalido, intente otra vez')
    for i in range(len(lista)):
        empleado_n = lista[i].split('//')
        if nombre==empleado_n[0]:
            print("Empleado registrado")
            temp=True
    if temp == False:
        print('Empleado no registrado')
        q = val_int('Desea registrarlo: \n1. Si \n2.No \n==> ', "Opcion invalida, intente otra vez", 3)
        if q == 1:
            registrar_empleado(nombre)
        if q==2:
            pass

def mostrar_empleados(lista):
    for i in range(len(lista)):
        print(f'''\n ------------------------ {i+1} ------------------------ ''')
        lista[i].mostrar_persona()

def eliminar_empleado(n):
    with open("C:\\Users\\Jsantos\Desktop\\CLASES ALGORITMOS\\Parcial II practicas\\CRUD\\registro_empleados.txt") as dbe:
        datos = dbe.readlines()
        borrar = datos[n-1]
        empleado_eliminado=borrar[:-1].split('//')
    with open("C:\\Users\\Jsantos\Desktop\\CLASES ALGORITMOS\\Parcial II practicas\\CRUD\\registro_empleados.txt", 'w') as dbe:
        for i in datos:
            if i != borrar:
                dbe.write(i)
    
    print(f'''\nEl empleado {empleado_eliminado[0]} ha sido eliminado correctamente. ''')


   
        


    







    

    
        


