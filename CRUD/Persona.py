class Persona:
    def __init__(self, nombre, edad, genero, cedula, cargo, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.cedula = cedula
        self.cargo = cargo
        self.sueldo = sueldo

    def mostrar_persona(self):
        print(f'''Nombre: {self.nombre} 
        Edad: {self.edad}
        Genero: {self.genero}
        Cedula: {self.cedula}
        Cargo: {self.cargo}
        Sueldo: {self.sueldo}''')
