from tools import *

def main():
    db=[]
    dbe=[]
    db = cargar_datos("C:\\Users\\Jsantos\Desktop\\CLASES ALGORITMOS\\Parcial II practicas\\CRUD\\registro_empleados.txt", db)
    dbe=cosificacion_empleados(db,dbe)
    
   
main()