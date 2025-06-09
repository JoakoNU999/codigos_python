gente={}
def ingresar():
    rut=input("Ingrese RUT: ")
    nombre=input("Ingrese nombre: ")
    edad=int(input("Ingrese edad: "))
    if rut in gente:
        print("ese rut ya existe")
    else:
        gente[rut]=[nombre,edad]
        print("Agregado")
def listar():
    for key,value in gente.items():
        print(f"Rut:{key} - Nombre:{value[0]} - Edad:{value[1]}")
ciclo=True
while ciclo:
    print("""
          1- Ingresar
          2- Listae
          3-Salir
          """)
    op=int(input("Ingrese Opcion"))
    match op:
        case 1:
            ingresar()
        case 2:
            listar()
        case 3:
            ciclo=False