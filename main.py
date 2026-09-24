from paciente import Paciente
pacientes:list[Paciente]=[
        Paciente("13.407.234-4","Fernando De La Rain",20,"Fonasa"),
        Paciente("17.540.231-9","Maria Troncoso",1000,"Isapre"),
        Paciente("0-0","La rica Ñonga",300000000000,"Otro"),
        Paciente("0.000.000-0","Queri Todo",-10000000,"Otro"),
        Paciente("II.III.III-I","Maria Conchita Alonso","2000 Antes A.C","Otro")
    ]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un numero entero.")

def menu():
    print("="*20)
    print("Menu Clinica")
    print("="*20)
    print("1.- Agregar paciente")
    print("2.- editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op=leer_numero("Ingrese una opcion: ")                                       
    return op


def agregar_paciente()->None:
    rut=input("Ingrese RUT del paciente: ")
    nombre=input("Ingrese nombre del paciente: ")
    edad=leer_numero("Ingrese edad del paciente: ")
    print("Seleccione prevision del paciente: ")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-Particular")
    print("4.-Otro")
    op=leer_numero("Seleccione una prevision del paciente: ")
    if op==1:
        prevision="Fonasa"
    elif op==2:
        prevision="Isapre"
    elif op==3:
        prevision="Particular"
    elif op==4:
        prevision="Otro"

    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    print("Paciente agregado ")
    print(f"Total de pacientes: {len(pacientes)}")

def imprimir_pacientes()->None:
    if len(pacientes)==0:
        print("No hay paciente")
    else:
        for paciente in pacientes:
            print(paciente)
            print("-"*20)

def buscar_paciente()->Paciente:
    rut=input("Ingrese RUT del paciente: ")
    for p in pacientes:
        if p.rut==rut:
            return p
        print("Paciente no encontrado.")
        return None

def imprimir_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontro el paciente.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        paciente.remove(paciente)
        print("Paciente eliminado")
    else:
        print("No se encontro el paciente.")

def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("menu de edicion")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar prevision")
        print("0.-Salir")
        op=leer_numero("Ingrese una opcion: ")
        if op==1:
            nombre_nuevo=input("Ingrese nuevo nombre: ")
            paciente.nombre=nombre_nuevo
            print("Nombre actualizado")
        elif op==2:
            edad_nueva=leer_numero("Ingrese nueva edad: ")
            paciente.edad=edadf_nueva
            print("Edad actualizada")
        elif op==3:
            print("Tipos de prevision: ")
            print("Fonasa")
            print("Isapre")
            print("Particular")
            print("Otro")
            op=leer_numero("Seleccione una prevision: ")
            if op==1:
                paciente.prevision="Fonasa"
                print("Prevision actualizada")
            if op==2:
                paciente.prevision="Isapre"
                print("Prevision actualizada")
            if op==3:
                paciente.prevision="Particular"
                print("Prevision actualizada")
            if op==4:
                paciente.prevision="Otro"
                print("Prevision actualizada")
            else:
                print("Opcion invalida")
    else:
        print("No se encuentra el paciente")

def main():
    while True:
        opcion=menu()
        if opcion==1:
            print("Agregar paciente")
            agregar_paciente()
        elif opcion==2:
            print("Editar paciente")
        elif opcion==3:
            print("Eliminar paciente")
        elif opcion==4:
            print("Mostrar un paciente")
            imprimir_pacientes()
        elif opcion==5:
            print("Mostrar todos los pacientes")
            imprimir_paciente()
        elif opcion==0:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

#def main():
    #opcion=menu()
    #print(f"opcion seleccionada: {opcion}")

    # creando objeto paciente
    #p1=Paciente("22.222.113-5","Pedro Pascal",300000,"Fonasa")
    #print(p1)


if __name__=="__main__":
    main()